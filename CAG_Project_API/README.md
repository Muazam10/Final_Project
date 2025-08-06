# **Final Project of [AWFERA](https://awfera.com/) Python Programming Course**

# CAG Project API: Chat With Your PDF

The **CAG Project API** is a FastAPI-based application designed to allow users to upload PDF files, extract text from them, store the extracted content, and query it using a Large Language Model (LLM) powered by Google Gemini. The application provides a simple REST API for managing PDF data and retrieving context-aware responses based on user queries.

## Features

- **PDF Upload and Text Extraction**: Upload PDF files, extract their text content using PyPDF, and store it in an in-memory data store (extendable to a database).
- **LLM Integration**: Query the stored PDF content using Google Gemini to generate context-aware responses.
- **CRUD Operations**: Create, update, query, and delete PDF data associated with unique UUIDs.
- **RESTful API**: Built with FastAPI, providing a clean and documented interface via Swagger UI.
- **Temporary File Management**: Safely handles uploaded PDF files with automatic cleanup.
- **Environment Configuration**: Uses `.env` for secure API key management.

## Project Structure

```
CAG_Project_API/
├── src/
│   ├── routers/
│   │   └── data_handler.py       # FastAPI router for handling PDF uploads, updates, queries, and deletions
│   ├── utils/
│   │   ├── pdf_processor.py      # Utility for extracting text from PDFs using PyPDF
│   │   └── llm_client.py         # Utility for interacting with Google Gemini API
│   └── data_store.py             # In-memory data store (mock database)
├── .env                          # Environment variables (e.g., GEMINI_API_KEY)
├── main.py                       # FastAPI application entry point
├── requirements.txt              # Project dependencies
└── README.md                     # Project documentation
```

## Prerequisites

- Python 3.8+
- A Google Gemini API key (obtain from [Google AI Studio](https://aistudio.google.com))

## Usage

### API Endpoints

The API is accessible under the `/api/v1` prefix. Below are the main endpoints:

1. **POST `/api/v1/upload/{uuid}`**:
   - Upload a PDF file associated with a UUID.
   - Extracts text and stores it in the in-memory data store.
   - **Example**:
     ```bash
     curl -X POST "http://127.0.0.1:8001/api/v1/upload/123e4567-e89b-12d3-a456-426614174000" -F "file=@sample.pdf"
     ```

2. **PUT `/api/v1/update/{uuid}`**:
   - Append text from a new PDF to an existing UUID's data.
   - **Example**:
     ```bash
     curl -X PUT "http://127.0.0.1:8001/api/v1/update/123e4567-e89b-12d3-a456-426614174000" -F "file=@new_sample.pdf"
     ```

3. **GET `/api/v1/query/{uuid}?query={user_query}`**:
   - Query the stored text for a UUID using Google Gemini.
   - **Example**:
     ```bash
     curl "http://127.0.0.1:8001/api/v1/query/123e4567-e89b-12d3-a456-426614174000?query=What is the main topic of the document?"
     ```

4. **DELETE `/api/v1/data/{uuid}`**:
   - Delete the data associated with a UUID.
   - **Example**:
     ```bash
     curl -X DELETE "http://127.0.0.1:8001/api/v1/data/123e4567-e89b-12d3-a456-426614174000"
     ```

5. **GET `/api/v1/list_uuids`**:
   - List all UUIDs in the data store.
   - **Example**:
     ```bash
     curl "http://127.0.0.1:8001/api/v1/list_uuids"
     ```

6. **GET `/`**:
   - Returns a simple HTML welcome page with a link to the Swagger UI.

### Example Workflow

1. Upload a PDF with a UUID:
   ```bash
   curl -X POST "http://127.0.0.1:8001/api/v1/upload/123e4567-e89b-12d3-a456-426614174000" -F "file=@document.pdf"
   ```

2. Query the content:
   ```bash
   curl "http://127.0.0.1:8001/api/v1/query/123e4567-e89b-12d3-a456-426614174000?query=Summarize the document"
   ```

3. Append more content:
   ```bash
   curl -X PUT "http://127.0.0.1:8001/api/v1/update/123e4567-e89b-12d3-a456-426614174000" -F "file=@additional.pdf"
   ```

4. Delete the data:
   ```bash
   curl -X DELETE "http://127.0.0.1:8001/api/v1/data/123e4567-e89b-12d3-a456-426614174000"
   ```

## Dependencies

The project uses the following Python packages (listed in `requirements.txt`):
- `fastapi`: For building the REST API.
- `uvicorn[standard]`: ASGI server for running FastAPI.
- `python-multipart`: For handling file uploads.
- `pypdf`: For extracting text from PDF files.
- `google-genai`: For interacting with the Google Gemini API.
- `python-dotenv`: For loading environment variables.