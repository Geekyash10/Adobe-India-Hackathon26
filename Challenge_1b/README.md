# 📄 Adobe India Hackathon 2026 – Challenge 1B

This repository contains the solution to **Challenge 1B** of the Adobe India Hackathon 2026. The objective is to build a semantic document understanding system that extracts and ranks the most relevant sections of a PDF document based on a user query.

---

## 🧠 Problem Statement

Given a query and a PDF document, extract relevant sections from the document and rank them in terms of importance using natural language understanding techniques. The output should be structured in a JSON format that lists the document title, outline, and top-ranked relevant sections.

---

## 🚀 Solution Overview

Our system follows this pipeline:

1. **Text Extraction**: Extracts blocks of text and metadata from PDFs using `PyMuPDF`.
2. **Heading Detection**: Identifies section headings using heuristics (length, formatting, structure).
3. **Embedding**: Encodes all sections using `SentenceTransformer` (`all-MiniLM-L6-v2`).
4. **Similarity Ranking**: Ranks sections by cosine similarity to the user query.
5. **Output Generation**: Creates a JSON response with the document title, outline, and top-k relevant sections.

---


---

## 🛠️ Setup Instructions

### ✅ Requirements

- Python 3.8+
- pip
- Git (for cloning the repo)

### ⚙️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Geekyash10/Adobe-India-Hackathon26.git
   cd Adobe-India-Hackathon26/Challenge_1b
   pip install -r requirements.txt
   from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('all-MiniLM-L6-v2')
    model.save('models/all-MiniLM-L6-v2')

2. **Docker Setup**
   ```bash
    docker build -t adobe-challenge-1b .
    docker run -v $(pwd)/inputs:/app/inputs -v $(pwd)/outputs:/app/outputs adobe-challenge-1b
2. **Docker Setup**
   ```bash
     {
      "title": "Understanding Neural Networks",
      "outline": [
        {
          "heading": "Introduction",
          "page": 1
        },
        {
          "heading": "Training Methods",
          "page": 3
        }
      ],
      "top_sections": [
        {
          "document": "neural_networks.pdf",
          "section_title": "Backpropagation and Gradient Descent",
          "importance_rank": 1,
          "page_number": 4,
          "score": 0.9021
        },
        {
          "document": "neural_networks.pdf",
          "section_title": "Activation Functions Overview",
          "importance_rank": 2,
          "page_number": 2,
          "score": 0.8754
        }
      ]
    }



