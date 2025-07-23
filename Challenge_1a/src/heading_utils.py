import re

def clean_text(text):
    return re.sub(r'\s+', ' ', text.strip())

def is_valid_heading(text):
    text = clean_text(text)
    return (
        2 <= len(text) <= 150 and
        len(text.split()) <= 20 and
        any(c.isalpha() for c in text) and
        not text.isdigit() and
        sum(c.isalnum() or c.isspace() for c in text) / len(text) >= 0.6 and
        not re.match(r'^(page|figure|table)\s+\d+', text, re.IGNORECASE)
    )

def classify_headings(blocks):
    if not blocks:
        return "", []

    font_sizes = sorted({b["font_size"] for b in blocks}, reverse=True)
    h1_size = font_sizes[0] if len(font_sizes) > 0 else None
    h2_size = font_sizes[1] if len(font_sizes) > 1 else None
    h3_size = font_sizes[2] if len(font_sizes) > 2 else None

    title = next((b["text"] for b in blocks if b["y"] < 150 and b["font_size"] == h1_size), "")

    seen = set()
    outline = []
    for b in sorted(blocks, key=lambda x: (x["page"], x["y"])):
        text = clean_text(b["text"])
        if not is_valid_heading(text) or text == title:
            continue

        level = None
        if b["font_size"] == h1_size and b["y"] < 600:
            level = "H1"
        elif h2_size and b["font_size"] == h2_size and b["y"] < 700:
            level = "H2"
        elif h3_size and b["font_size"] == h3_size:
            level = "H3"

        if level:
            key = (level, text, b["page"])
            if key not in seen:
                seen.add(key)
                outline.append({"level": level, "text": text, "page": b["page"]})

    return title, outline
