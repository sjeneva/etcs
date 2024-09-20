from serpapi import GoogleSearch
import pandas as pd

params = {
  "engine": "google_news",
  "q": "ESG Logistics",
  "api_key": "f61c7f73d7908348b320cb0808e3f2c236ba42fc0994ec204ac9dca3dfc43b76"
}

search = GoogleSearch(params)
results = search.get_dict()
news_results = results["news_results"]

# Prepare the data for DataFrame
data_for_df = []
for news_item in news_results:
    # Extract necessary information from each news item
    data_for_df.append({
        'Title': news_item.get('title'),
        'Link': news_item.get('link'),
        'Source': news_item.get('source', {}).get('title', 'Unknown source'),
        'Snippet': news_item.get('snippet'),
        'Publication Date': news_item.get('date', 'Unknown date')
        # Add more fields here as needed
    })

# Convert list of dictionaries to DataFrame
df = pd.DataFrame(data_for_df)

# Define the path for the Excel file
excel_path = 'ESG_Logistics_google_news_results.xlsx'

# Save the DataFrame to an Excel file
df.to_excel(excel_path, index=False, engine='openpyxl')

print(f"News results have been saved to {excel_path}")
