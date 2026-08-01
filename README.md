# Notes API

A REST API built with Python and FastAPI to create, read, update and delete notes.

## Tech Stack
- Python
- FastAPI
- SQLite (coming soon)

## Endpoints
- POST /notes — create a note
- GET /notes — get all notes
- GET /notes/{id} — get one note
- PUT /notes/{id} — update a note
- DELETE /notes/{id} — delete a note

## How to run
1. Install packages: pip install fastapi uvicorn
2. Run: python -m uvicorn main:app --reload
3. Open: http://127.0.0.1:8000/docs
