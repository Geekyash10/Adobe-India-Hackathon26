FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy and install only safe dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
# Download NLTK punkt tokenizer

COPY . .

ENV NLTK_DATA=/usr/local/nltk_data
RUN python -m nltk.downloader -d /usr/local/nltk_data punkt punkt_tab

# Preload and cache the sentence-transformer model (MiniLM)
RUN python -c "\
from sentence_transformers import SentenceTransformer; \
SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2').save('./models/all-MiniLM-L6-v2')"


CMD ["python", "main.py"]
