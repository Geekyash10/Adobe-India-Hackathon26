# src/processor.py
import os
import json
from datetime import datetime
from src.pdf_parser import extract_text_blocks
from src.embedder import Embedder
from src.summarizer import summarize

def process_collection(collection_path):
    # Load input JSON
    input_path = os.path.join(collection_path, "challenge1b_input.json")
    with open(input_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    persona = config["persona"]["role"]
    task = config["job_to_be_done"]["task"]
    query = f"{persona}: {task}"
    documents = config["documents"]
    
    all_sections = []
    for doc in documents:
        pdf_path = os.path.join(collection_path, "PDFs", doc["filename"])
        blocks = extract_text_blocks(pdf_path)
        for b in blocks:
            b["document"] = doc["filename"]
            all_sections.append(b)

    # Embed & Rank
    embedder = Embedder()
    top_sections = embedder.rank_sections(query, all_sections, top_k=5)

    # Generate refined analysis
    refined = []
    for section in top_sections:
        matching = next(
            (s for s in all_sections if s["document"] == section["document"]
             and s["page"] == section["page_number"]
             and s["text"].startswith(section["section_title"][:20])), None)
        if matching:
            refined_text = summarize(matching["text"])
            refined.append({
                "document": matching["document"],
                "page_number": matching["page"],
                "refined_text": refined_text
            })

    # Output JSON
    output = {
        "metadata": {
            "input_documents": [d["filename"] for d in documents],
            "persona": persona,
            "job_to_be_done": task,
            "timestamp": datetime.now().isoformat()
        },
        "extracted_sections": top_sections,
        "subsection_analysis": refined
    }

    output_path = os.path.join(collection_path, "challenge1b_output.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
