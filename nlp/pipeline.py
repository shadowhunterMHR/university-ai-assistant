# nlp/pipeline.py

from .load_data import load_scraped_data
from .preprocess import clean_text
from .ner import extract_entities
from .tfidf import TfidfSearch
from .intent import classify_intent

def run_pipeline(user_query):
    texts, urls = load_scraped_data()
    cleaned_texts = [clean_text(t) for t in texts]

    tfidf_engine = TfidfSearch(cleaned_texts)
    top_indices, scores = tfidf_engine.search(user_query)

    relevant_docs = [texts[i] for i in top_indices]
    relevant_urls = [urls[i] for i in top_indices]

    entities = extract_entities(user_query)
    intent = classify_intent(user_query)

    return {
        "intent": intent,
        "entities": entities,
        "documents": relevant_docs,
        "urls": relevant_urls
    }
