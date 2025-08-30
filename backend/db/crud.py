from .models import Note
from .config import SessionLocal
from .embeddings import embedder

def add_note(content: str):
    session = SessionLocal()
    embedding = embedder.encode(content).tolist()
    note = Note(content=content, embedding=embedding)
    session.add(note)
    session.commit()
    session.close()

def search_notes(query: str, k: int = 5):
    session = SessionLocal()
    query_embedding = embedder.encode(query).tolist()
    results = (
        session.query(Note)
        .order_by(Note.embedding.cosine_distance(query_embedding))
        .limit(k)
        .all()
    )
    session.close()
    return [{"content": r.content, "source": r.source} for r in results]
