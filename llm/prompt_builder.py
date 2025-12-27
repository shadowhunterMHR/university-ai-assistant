def build_prompt(query, intent, entities, documents):
    context = "\n\n".join(documents[:3])

    entity_text = ", ".join([e["text"] for e in entities]) or "None"

    prompt = f"""
You are an intelligent university information assistant.

User Query:
{query}

Detected Intent:
{intent}

Extracted Entities:
{entity_text}

Relevant University Information:
{context}

Instructions:
- Answer ONLY from the given information
- Be clear and concise
- Do not guess or hallucinate
- If information is missing, say so

Final Answer:
"""
    return prompt
