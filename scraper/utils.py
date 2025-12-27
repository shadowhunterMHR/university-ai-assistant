# scraper/utils.py

from urllib.parse import urlparse, urljoin

def is_internal_link(base_url, link):
    base_domain = urlparse(base_url).netloc
    link_domain = urlparse(link).netloc
    return base_domain == link_domain or link_domain == ""

def clean_url(base_url, link):
    return urljoin(base_url, link.split("#")[0])
