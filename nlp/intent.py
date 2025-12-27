# nlp/intent.py

def classify_intent(query):
    query = query.lower()

    if any(word in query for word in ["fee", "cost", "charges"]):
        return "FEES"

    if any(word in query for word in ["admission", "apply", "eligibility"]):
        return "ADMISSION"

    if any(word in query for word in ["faculty", "professor", "teacher"]):
        return "FACULTY"

    if any(word in query for word in ["program", "degree", "course"]):
        return "PROGRAM"

    return "GENERAL"
