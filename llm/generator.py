# llm/generator.py
from .model import generate_text
from .prompt_builder import build_prompt

def generate_answer(query, intent, entities, documents, api_token=None):
    prompt = build_prompt(query, intent, entities, documents)
    response = generate_text(prompt, token=api_token)
    return response.strip()
