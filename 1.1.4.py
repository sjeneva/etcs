from GoogleNews import GoogleNews
import pandas as pd
from dateparser import parse  # Import dateparser to handle various date formats

# List of keywords to search
keywords = [
    "logistics sustainability",
    "green logistics",
    "sustainable transportation",
    "eco-friendly shipping",
    "carbon footprint in logistics",
    "ESG logistics",
    "renewable energy logistics",
    "electric vehicles in logistics",
    "logistics carbon emissions",
    "circular economy in logistics"
]

# Initialize Google News object without time restriction
googlenews = GoogleNews(period='')  # Empty period to remove date restriction

# Create an empty list to store all articles
all_articles = []

# Loop through each keyword and fetch results
for keyword in keywords:
    googlenews.clear()  # Clear previous results before each search
    googlenews.search(keyword)

    # Fetch results
    results = googlenews.result()

    # Extract required information
    for result in results:
        raw_date = result.get('date')
        title = result.get('title')
        publisher = result.get('media')
        link = result.get('link')

        # Parse date to include month and year
        parsed_date = parse(raw_date, settings={'TIMEZONE': 'UTC'})
        formatted_date = parsed_date.strftime('%B %Y') if parsed_date else 'Unknown'

        all_articles.append([formatted_date, title, publisher, link])

# Create DataFrame
df = pd.DataFrame(all_articles, columns=['Date', 'Title', 'Publisher', 'URL'])

# Save to CSV
df.to_csv('expanded_google_news_articles_1.csv', index=False)

print("Data saved to expanded_google_news_articles_1.csv")
