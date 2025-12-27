# scraper/parser.py

from bs4 import BeautifulSoup

def extract_text_and_links(html):
    soup = BeautifulSoup(html, "lxml")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator=" ")
    text = " ".join(text.split())

    links = set()
    for a in soup.find_all("a", href=True):
        links.add(a["href"])

    return text, links
