# test.py
import os
from nlp.pipeline import run_pipeline
from llm.generator import generate_answer

if __name__ == "__main__":
    query = "What are the admission requirements for BS Computer Science?"
    nlp_result = run_pipeline(query)

    API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
    if not API_TOKEN:
        raise ValueError("Hugging Face API token not found. Set HUGGINGFACE_API_TOKEN env variable.")

    answer = generate_answer(
        query=query,
        intent=nlp_result["intent"],
        entities=nlp_result["entities"],
        documents=nlp_result["documents"],
        api_token=API_TOKEN
    )

    print("\nFINAL ANSWER:\n")
    print(answer)
