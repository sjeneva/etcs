import json
import pandas as pd
from serpapi import GoogleSearch
import re

def fetch_results(params):
    search = GoogleSearch(params)
    results = search.get_dict()
    return results.get("organic_results", [])

def get_serpapi_news_data(query, api_key, location="United States", pages=1):
    all_data = []
    for page in range(pages):
        print(f"Fetching page {page + 1}")
        params = {
            "engine": "google_news",
            "q": "ESG Logistics",
            "api_key": "f61c7f73d7908348b320cb0808e3f2c236ba42fc0994ec204ac9dca3dfc43b76",
            "location": "United States",
            "hl": "en",
            "gl": "US",
            "start": page * 50
        }
        page_data = fetch_results(params)
        if not page_data:
            print("No more data found.")
            break
        all_data.extend(page_data)
    return all_data

api_key = "f61c7f73d7908348b320cb0808e3f2c236ba42fc0994ec204ac9dca3dfc43b76"
query = "ESG Logistics"
pages_to_fetch = 50

organic_results = get_serpapi_news_data(query, api_key, pages=pages_to_fetch)

data_for_df = []
for result in organic_results:
    # Assuming 'title' and 'link' are directly available
    title = result.get('title')
    link = result.get('link')

    # Extracting the source and publication date if available
    source = result.get('source', {}).get('title', 'Unknown source')
    publication_date = result.get('date', 'Unknown date')

    data_for_df.append({
        'Title': title,
        'Link': link,
        'Source': source,
        'Publication Date': publication_date,
        # Include other fields as needed
    })

df = pd.DataFrame(data_for_df)
excel_path = 'ESG_Logistics_google_news_results.xlsx'
df.to_excel(excel_path, index=False)

print(f"Results have been saved to {excel_path}")

