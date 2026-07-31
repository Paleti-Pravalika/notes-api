from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

notes = []
note_id_counter = 1

class Note(BaseModel):
    title: str
    content: str

@app.get("/")
def home():
    return {"message": "Notes API is running!"}

@app.post("/notes")
def create_note(note: Note):
    global note_id_counter
    new_note = {
        "id": note_id_counter,
        "title": note.title,
        "content": note.content
    }
    notes.append(new_note)
    note_id_counter += 1
    return new_note
# GET all notes
@app.get("/notes")
def get_all_notes():
    return notes
# UPDATE a note
@app.put("/notes/{note_id}")
def update_note(note_id: int, updated_note: Note):
    for note in notes:
        if note["id"] == note_id:
            note["title"] = updated_note.title
            note["content"] = updated_note.content
            return note
    return {"error": "Note not found"}

# DELETE a note
@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    for index, note in enumerate(notes):
        if note["id"] == note_id:
            notes.pop(index)
            return {"message": "Note deleted successfully"}
    return {"error": "Note not found"}