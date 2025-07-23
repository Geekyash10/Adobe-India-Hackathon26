import fitz  # PyMuPDF

def extract_text_blocks(pdf_path):
    doc = fitz.open(pdf_path)
    extracted = []

    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for block_idx, block in enumerate(blocks):
            if "lines" not in block:
                continue
            for line_idx, line in enumerate(block["lines"]):
                line_text = ""
                font_sizes = []
                for span in line["spans"]:
                    if span["text"].strip():
                        line_text += span["text"]
                        font_sizes.append(span["size"])

                if line_text.strip() and font_sizes:
                    extracted.append({
                        "text": line_text.strip(),
                        "font_size": max(font_sizes),
                        "page": page_num + 1,
                        "y": block["bbox"][1],
                        "x": block["bbox"][0],
                        "block_idx": block_idx,
                        "line_idx": line_idx
                    })

    doc.close()
    return extracted

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []

    toc = doc.get_toc()  # Table of contents
    for entry in toc:
        level, title, page = entry
        outline.append({
            "level": f"H{level}",
            "text": title.strip(),
            "page": page
        })

    doc.close()
    return outline