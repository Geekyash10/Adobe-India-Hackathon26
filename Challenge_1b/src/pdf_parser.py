# src/pdf_parser.py
import fitz  # PyMuPDF
import re

def clean_text(text):
    return re.sub(r'\s+', ' ', text.strip())

def extract_text_blocks(pdf_path):
    doc = fitz.open(pdf_path)
    blocks = []
    for page_num, page in enumerate(doc, start=1):
        blocks_info = page.get_text("dict")["blocks"]
        for block in blocks_info:
            if "lines" not in block:
                continue
            text = ""
            for line in block["lines"]:
                for span in line["spans"]:
                    text += span["text"] + " "
            text = clean_text(text)
            if len(text) > 30:
                blocks.append({
                    "page": page_num,
                    "text": text,
                    "bbox": block["bbox"],
                    "size": span["size"]
                })
    return blocks
