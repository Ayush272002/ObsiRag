from .vectorstore import get_vectorstore

vectorstore = get_vectorstore()
retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

def get_top_k_notes(query: str, k: int = 5):
    """
    Returns top-k notes for a query.
    result is a dict: {"content": ..., "source": ...}
    """
    results = retriever.get_relevant_documents(query)
    return [{"content": r.page_content, "source": r.metadata.get("source")} for r in results]