def chunk_ocr(ocr_result, page_num):
    chunks = []
    for line in ocr_result:
        chunks.append({
            "text": line[1][0],
            "page": page_num,
            "confidence": round(line[1][1], 2)
        })
    return chunks
