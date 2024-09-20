import json
import pandas as pd
from serpapi import GoogleSearch

def fetch_results(params):
    search = GoogleSearch(params)
    results = search.get_dict()
    return results["organic_results"] if "organic_results" in results else []

def get_serpapi_news_data(query, api_key, location, pages=1):
    all_data = []
    for page in range(pages):
        print(f"Fetching page {page + 1}")
        params = {
            "engine": "google_news",
            "q": "ESG Logistics",
            "api_key": "f61c7f73d7908348b320cb0808e3f2c236ba42fc0994ec204ac9dca3dfc43b76",
            "location": "United States",  # Specifying the United States as the location
            "hl": "en",  # Setting the language to English
            "gl": "US",  # Specifying the country to United States
            "start": page * 100  # Adjust according to the pagination limits of Google News
        }
        page_data = fetch_results(params)
        if not page_data:
            print("No more data found.")
            break
        all_data.extend(page_data)
    return all_data

api_key = "f61c7f73d7908348b320cb0808e3f2c236ba42fc0994ec204ac9dca3dfc43b76"
query = "CESG Logistics"
pages_to_fetch = 100  # Example: Fetch first 2 pages

# Fetch data from SerpAPI
organic_results = get_serpapi_scholar_data(query, api_key, pages=pages_to_fetch)

# Process and save data
# Prepare the data for DataFrame
data_for_df = []  # Make sure this line is aligned with the 'for' statement below
for result in organic_results:
    publication_info_summary = result.get('publication_info', {}).get('summary', '')
    # The publication_info summary might include the date and publisher but in a combined string format.

    # Attempt to extract publication year as a simple approach (assuming it's a 4-digit number in the summary).
    # This is a naive extraction and might not work for all cases.
    import re

    publication_year_match = re.search(r'\b\d{4}\b', publication_info_summary)
    publication_year = publication_year_match.group(0) if publication_year_match else 'Not available'

    # Assuming the publisher might not be separately available, you might need to parse it from the summary or another field.
    # This is highly dependent on how the information is structured and might not be straightforward.

    # Here, we're focusing on what's directly extractable or inferable:
    paper_info = {
        'position': result.get('position'),
        'title': result.get('title'),
        'result_id': result.get('result_id'),
        'link': result.get('link'),
        'snippet': result.get('snippet'),
        'publication_summary': publication_info_summary,  # This contains a mix of publication info
        'publication_year': publication_year,  # Extracted or inferred publication year
        'authors': ', '.join([author.get('name') for author in result.get('publication_info', {}).get('authors', [])]),
        'cited_by': result.get('inline_links', {}).get('cited_by', {}).get('total'),
        'related_pages_link': result.get('inline_links', {}).get('related_pages_link'),
        'versions': result.get('inline_links', {}).get('versions', {}).get('total')
    }
    data_for_df.append(paper_info)

# Convert list of dictionaries to DataFrame
df = pd.DataFrame(data_for_df)

# Save the DataFrame to an Excel file
excel_path = 'ESG_Logistics_google_news.xlsx'
df.to_excel(excel_path, index=False)

print(f"Results have been saved to {excel_path}")
