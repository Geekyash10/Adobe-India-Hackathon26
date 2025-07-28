# main.py
import os
from src.processor import process_collection

def run_all_collections(base_path="Collections"):
    for folder in os.listdir(base_path):
        path = os.path.join(base_path, folder)
        if os.path.isdir(path) and "challenge1b_input.json" in os.listdir(path):
            print(f"\n🟢 Processing: {folder}")
            process_collection(path)
        else:
            print(f"⚠️ Skipped: {folder} (missing input)")

if __name__ == "__main__":
    run_all_collections()
