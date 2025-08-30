from pydantic import BaseModel

class NoteIn(BaseModel):
    content: str