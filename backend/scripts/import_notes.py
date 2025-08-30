import os
import sys
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.config import SessionLocal
from db.models import Note
from sentence_transformers import SentenceTransformer

# Path obsidian notes folder
NOTES_DIR = Path("../../obsidian-notes/content").resolve()

embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def import_notes():
    session = SessionLocal()
    imported = 0
    skipped = 0

    for path in NOTES_DIR.rglob("*.md"):
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            if not content.strip():
                print(f"Skipping empty file: {path}")
                skipped += 1
                continue

            embedding = embedder.encode(content).tolist()
            rel_path = str(path.relative_to(NOTES_DIR))

            note = Note(
                content=content,
                embedding=embedding,
                source=rel_path,
            )
            session.add(note)
            imported += 1

        except Exception as e:
            print(f"❌ Error with {path}: {e}")
            skipped += 1

    session.commit()
    session.close()
    print(f"Imported {imported} notes, skipped {skipped}")

if __name__ == "__main__":
    import_notes()
