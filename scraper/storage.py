import pandas as pd
import os
from config import OUTPUT_FILE


def save_data(records):
    # Ensure directory exists
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    # Convert to DataFrame
    df = pd.DataFrame(records)

    # Save to CSV
    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")

    print(f"Saved {len(records)} pages to {OUTPUT_FILE}")
