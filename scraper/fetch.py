# scraper/fetch.py

import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (UniversityCrawler/1.0)"
}

def fetch_html(url):
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        res.raise_for_status()
        return res.text
    except Exception as e:
        print(f"[ERROR] {url} → {e}")
        return None
