from db.models import Note
from db.config import engine
from sqlalchemy.orm import sessionmaker
from langchain_core.documents import Document
from langchain_postgres import PGVector
from langchain_huggingface import HuggingFaceEmbeddings  

SessionLocal = sessionmaker(bind=engine)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def get_vectorstore():
    vectorstore = PGVector(
        collection_name="notes",
        connection=engine,
        embeddings=embeddings
    )

    session = SessionLocal()
    notes = session.query(Note).all()
    session.close()

    docs = [
        Document(page_content=n.content, metadata={"source": n.source})
        for n in notes
    ]

    if docs:
        vectorstore.add_documents(docs)

    return vectorstore