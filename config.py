# config.py

# =========================
# WEBSITE CONFIGURATION
# =========================

BASE_URL = "https://riphah.edu.pk"

ALLOWED_DOMAINS = [
    "riphah.edu.pk"
]

# =========================
# SCRAPER SETTINGS
# =========================

MAX_PAGES = 1000
REQUEST_DELAY = 1
TIMEOUT = 10

# =========================
# STORAGE
# =========================

OUTPUT_FILE = "data/scraped_data.csv"
