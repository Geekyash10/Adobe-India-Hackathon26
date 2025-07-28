# 📚 Document Processing Pipeline 🚀

This project provides a comprehensive solution for processing document collections, extracting relevant information, and generating summaries. It's designed to handle PDF documents, extract text, identify key sections, and provide concise summaries based on a given query. This README provides a detailed overview of the project, its features, setup instructions, and how to contribute.

## ✨ Key Features

- **Directory Traversal:** Automatically scans specified directories for document collections. 📂
- **Configuration Loading:** Loads processing configurations from JSON files. ⚙️
- **PDF Extraction:** Extracts text blocks from PDF documents. 📄
- **Semantic Embedding:** Generates text embeddings using Sentence Transformers. 🧠
- **Section Ranking:** Ranks document sections based on semantic similarity to a query. 🥇
- **Text Summarization:** Summarizes the top-ranked sections using the TextRank algorithm. 📝
- **Output Generation:** Creates JSON output files containing metadata, ranked sections, and summaries. 📤
- **Heading Classification:** Identifies and classifies headings within documents for improved structure. 🔖
- **Outline Extraction:** Extracts existing outlines from PDFs or generates them from classified headings. 🌳

## 🛠️ Tech Stack

| Category    | Technology                      | Version (if specified) | Description                                                                 |
|-------------|---------------------------------|------------------------|-----------------------------------------------------------------------------|
| **Language** | Python                          | 3.x                    | The primary programming language used for the project.                       |
| **PDF Parsing** | PyMuPDF (fitz)                  | N/A                    | Used for opening, parsing, and extracting text from PDF files.             |
| **NLP**       | Sentence Transformers           | 2.2.2                  | Used for generating text embeddings.                                        |
|             | scikit-learn                    | N/A                    | Used for calculating cosine similarity between embeddings.                  |
|             | sumy                            | N/A                    | Used for text summarization using the TextRank algorithm.                   |
|             | nltk                            | N/A                    | Natural Language Toolkit, used by Sumy for text processing.                |
| **Data Handling** | json                            | N/A                    | Used for loading and saving JSON data.                                    |
| **Other**     | os                              | N/A                    | Used for interacting with the operating system (file system operations). |
|             | re                              | N/A                    | Used for regular expression operations (text cleaning).                    |
|             | datetime                        | N/A                    | Used for generating timestamps in the output.                               |
| **Hugging Face** | huggingface_hub | 0.14.1 | Used for accessing pre-trained models. |

## 📦 Getting Started

### Prerequisites

- Python 3.6+
- `pip` package installer

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate.bat  # On Windows
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Running Locally

1.  **Place your PDF documents in the `Challenge_1a/input` directory.**
2.  **Ensure you have a `challenge1b_input.json` file in each collection directory within the `Collections` directory.**
3.  **Run the main script:**

    For Challenge 1a:

    ```bash
    python Challenge_1a/src/extractor.py
    ```

    For Challenge 1b:

    ```bash
    python Challenge_1b/main.py
    ```

4.  **The output JSON files will be generated in the `Challenge_1a/output` directory for Challenge 1a and within each collection directory for Challenge 1b.**

## 📂 Project Structure

```
├── Challenge_1a/
│   ├── src/
│   │   ├── extractor.py       # Main entry point for Challenge 1a
│   │   ├── heading_utils.py   # Heading classification utilities
│   │   ├── pdf_utils.py       # PDF extraction utilities
│   ├── input/               # Directory for input PDF files (Challenge 1a)
│   ├── output/              # Directory for output JSON files (Challenge 1a)
├── Challenge_1b/
│   ├── src/
│   │   ├── embedder.py      # Text embedding and ranking
│   │   ├── pdf_parser.py    # PDF parsing utilities
│   │   ├── processor.py     # Core processing logic for Challenge 1b
│   │   ├── summarizer.py    # Text summarization utilities
│   ├── main.py              # Main entry point for Challenge 1b
├── Collections/           # Directory containing document collections for Challenge 1b
│   ├── Collection_1/      # Example collection directory
│   │   ├── challenge1b_input.json # Input configuration file
│   │   ├── document1.pdf
│   │   ├── document2.pdf
├── requirements.txt       # Project dependencies
└── README.md              # This file
```




