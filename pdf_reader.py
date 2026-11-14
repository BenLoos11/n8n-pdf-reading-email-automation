from pathlib import Path 
import random 
import fitz 
from fastapi import FastAPI, HTTPException 

app = FastAPI()

BOOKS_DIR = Path("/books")

@app.get("/health")
def health():
    return{"status": "ok"}

@app.get("/random-page")
def random_page():
    books = list(BOOKS_DIR.glob("*.pdf"))

    if not books:
        raise HTTPException(status_code=404, detail="No PDF books found")

    random.shuffle(books)

    for book in books:
        try:
            with fitz.open(book) as pdf:
                page_numbers = list(range(len(pdf)))
                random.shuffle(page_numbers)

                for page_index in page_numbers:
                    page_text = pdf[page_index].get_text().strip()

                    if page_text:
                        return {
                            "book": book.name, 
                            "page": page_index +1,
                            "total_pages": len(pdf),
                            "text": page_text
                        }

        except Exception:
            continue

    raise HTTPException(
        status_code=500,
        detail="Could not extract text from any PDF"
    )    
