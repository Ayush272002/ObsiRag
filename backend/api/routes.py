from fastapi import APIRouter
from rag.rag_agent import answer_query

router = APIRouter()

@router.post("/query")
def query(body: dict):
    q = body["q"]
    answer = answer_query(q, k=5)
    return {"answer": answer}

