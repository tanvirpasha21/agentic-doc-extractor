import sys
import json
from pathlib import Path
from paddleocr import PaddleOCR
from pdf2image import convert_from_path
from PIL import Image
import numpy as np

# ---------------------------
# Parameters
# ---------------------------
if len(sys.argv) < 2:
    print(json.dumps({"error": "No file path provided"}))
    sys.exit(1)

file_path = Path(sys.argv[1])
if not file_path.exists():
    print(json.dumps({"error": f"File {file_path} does not exist"}))
    sys.exit(1)

# ---------------------------
# Initialize OCR
# ---------------------------
ocr = PaddleOCR(use_textline_orientation=True, lang="en")

# ---------------------------
# Helper: Convert PDF to images
# ---------------------------
def load_pages(file_path):
    if file_path.suffix.lower() == ".pdf":
        images = convert_from_path(str(file_path))
        return images
    else:
        return [Image.open(file_path)]

# ---------------------------
# Main extraction
# ---------------------------
result = {"pages": 0, "chunks": []}
pages = load_pages(file_path)
result["pages"] = len(pages)

for i, page in enumerate(pages, start=1):
    # Convert PIL image to numpy array for PaddleOCR
    img_np = np.array(page)

    # OCR detection
    ocr_results = ocr.predict(img_np)  # <-- use predict()

    for line in ocr_results:
        for box, text, conf in line:
            chunk = {
                "text": text,
                "page": i,
                "confidence": float(conf),
                "bbox": [float(x) for x in box],
                "strategy": "ocr"
            }
            result["chunks"].append(chunk)

# ---------------------------
# Output JSON
# ---------------------------
print(json.dumps(result))
