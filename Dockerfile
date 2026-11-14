FROM python:3.12-slim

WORKDIR /app

RUN python -m pip install --no-cache-dir fastapi uvicorn pymupdf

COPY pdf_reader.py /app/pdf_reader.py

CMD ["uvicorn", "pdf_reader:app", "--host", "0.0.0.0", "--port", "8000"]
