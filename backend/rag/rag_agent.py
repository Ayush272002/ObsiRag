import os
import yaml
import logging
from groq import Groq
import logging.config
from typing import List, Dict
from dotenv import load_dotenv
from rag.retriever import get_top_k_notes

load_dotenv()

with open(os.path.join(os.path.dirname(__file__), '../logging.yml'), 'r') as f:
    config = yaml.safe_load(f)
logging.config.dictConfig(config)
logger = logging.getLogger("rag_agent")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_prompt(query: str, docs: List[Dict], max_context_chars: int = 3000) -> str:
    """
    A prompt for the LLM including top-k docs as context.
    """
    context_text = ""
    for doc in docs:
        snippet = doc["content"]
        if len(snippet) > 1000:
            snippet = snippet[:1000] + "..."
        context_text += f"\nSource: {doc['source']}\n{snippet}\n"

    context_text = context_text[-max_context_chars:]

    prompt = f"""You are an AI assistant. Use the following notes to answer the question. If the answer is not in the notes, respond with "I don't know."

Notes:{context_text}

Question: {query}
Answer:"""
    return prompt

def answer_query(query: str, k: int = 5, temperature: float = 1.0):
    logger.info(f"User entered question: {query}")
    docs = get_top_k_notes(query, k=k)
    logger.info(f"DB returned top {k} notes: {docs}")
    prompt = generate_prompt(query, docs)

    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_completion_tokens=8192,
        top_p=1,
        reasoning_effort="medium",
        stream=True,
        stop=None
    )

    answer = ""
    for chunk in completion:
        delta = chunk.choices[0].delta.content or ""
        logger.info(delta)
        answer += delta
    return answer