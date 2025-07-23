import os
import json
from pdf_utils import extract_text_blocks, extract_outline
from heading_utils import classify_headings

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def process_pdf(pdf_path, output_path):
    outline = extract_outline(pdf_path)
    title = outline[0]["text"] if outline else ""

    if not outline:
        blocks = extract_text_blocks(pdf_path)
        title, outline = classify_headings(blocks)

    output = {
        "title": title,
        "outline": outline
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

def main():
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".pdf"):
            input_pdf = os.path.join(INPUT_DIR, filename)
            output_json = os.path.join(OUTPUT_DIR, filename.replace(".pdf", ".json"))
            process_pdf(input_pdf, output_json)

if __name__ == "__main__":
    main()