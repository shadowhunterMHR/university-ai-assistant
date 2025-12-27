# nlp/load_data.py

import pandas as pd

def load_scraped_data(path="data/riphah_pages.csv"):
    df = pd.read_csv(path)
    return df["text"].tolist(), df["url"].tolist()
