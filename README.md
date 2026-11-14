# n8n PDF Reading Automation



An automated workflow that randomly selects a page containing extractable text from a PDF book and emails it using n8n and Gmail.



## How It Works



1. n8n runs on a daily schedule.

2. An HTTP Request calls the Python PDF Reader API.

3. The API selects a random PDF and page containing text.

4. n8n formats the book title, page number, and extracted text.

5. Gmail emails the selected page.



## Technologies



\- n8n â€“ Workflow automation

\- Python and FastAPI â€“ PDF reader API

\- PyMuPDF â€“ PDF text extraction

\- Docker Compose â€“ Container management

\- Gmail OAuth2 â€“ Email delivery



## Requirements



\- Docker Desktop

\- Docker Compose

\- Gmail account

\- Gmail OAuth2 credentials configured in n8n

\- PDF books containing extractable text



## Setup



### 1. Clone the repository



```powershell

git clone https://github.com/YOUR\_GITHUB\_USERNAME/n8n-pdf-reading-automation.git

cd n8n-pdf-reading-automation

```



### 2. Configure your PDF folder



```powershell

Copy-Item .env.example .env

notepad .env

```



Set BOOKS\_PATH to your local PDF folder:



```env

BOOKS\_PATH=C:/Path/To/Your/PDF/Books

```



### 3. Start Docker services



```powershell

docker compose up -d --build

```



Open n8n at http://localhost:5678.



### 4. Import the workflow



Import `workflows/Daily Book Page Email.public.json` into n8n.



Configure your own Gmail OAuth2 credentials and recipient address, then activate the workflow.



The example workflow is scheduled for 1 PM daily using the America/Chicago timezone.



## API Endpoints



| Endpoint | Description |

|---|---|

| `/health` | Checks whether the API is running |

| `/random-page` | Returns a randomly selected page containing extractable text |



## Limitations



\- Scanned PDFs without an extractable text layer are not supported without OCR.

\- Previously selected pages are not tracked, so duplicates are possible.

\- Each user must configure their own Gmail credentials.

\- PDF books and personal credentials are not included in this repository.



## Security



Local environment files, PDF documents, n8n data, and the original workflow export are excluded from the public repository.


