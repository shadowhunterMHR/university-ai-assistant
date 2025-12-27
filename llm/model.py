# llm/model.py
from huggingface_hub import InferenceClient

_client = None

def load_model(token=None):
    """
    Initialize the Hugging Face Inference client.
    """
    global _client
    if _client is None:
        if not token:
            raise ValueError("You must provide a Hugging Face API token.")
        _client = InferenceClient(token=token)
    return _client

def generate_text(prompt, token=None, model="mistralai/Mistral-7B-Instruct-v0.2", max_tokens=300):
    """
    Generate text using Hugging Face hosted model via chat completion.
    """
    client = load_model(token)

    # Build a single‑message list in chat format
    messages = [
        {"role": "user", "content": prompt}
    ]

    # Use the chat_completion task
    response = client.chat_completion(
        messages=messages,
        model=model,
        max_tokens=max_tokens
    )

    # Extract the assistant answer text
    return response.choices[0].message.content