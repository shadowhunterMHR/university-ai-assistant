from fetch import fetch_html
from parser import extract_text_and_links
from utils import is_internal_link, clean_url
from storage import save_data
from config import BASE_URL, MAX_PAGES
from tqdm import tqdm


def crawl():
    visited = set()
    to_visit = [BASE_URL]
    records = []

    with tqdm(total=MAX_PAGES, desc="Crawling Pages") as pbar:
        while to_visit and len(visited) < MAX_PAGES:
            current_url = to_visit.pop(0)

            if current_url in visited:
                continue

            visited.add(current_url)
            pbar.update(1)

            html = fetch_html(current_url)
            if not html:
                continue

            text, links = extract_text_and_links(html)

            records.append({
                "url": current_url,
                "text": text
            })

            for link in links:
                full_url = clean_url(BASE_URL, link)
                if (
                    is_internal_link(BASE_URL, full_url)
                    and full_url not in visited
                    and full_url not in to_visit
                ):
                    to_visit.append(full_url)

    save_data(records)


if __name__ == "__main__":
    crawl()
