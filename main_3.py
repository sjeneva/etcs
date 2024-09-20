from pygooglenews import GoogleNews
import pandas as pd

def get_titles(search):
    gn = GoogleNews(country='USA')
    stories = []
    search_result = gn.search(search)
    newsitem = search_result['entries']
    for item in newsitem:
        # Extract the published date. This might need adjustment based on actual data structure.
        # The published date is often available in a 'published' or similar attribute.
        published = item.get('published', 'Unknown Date')

        # Extract publisher information if available (this line might need adjustment as noted before)
        publisher = item.get('source', {}).get('title', 'Unknown Publisher')

        story = {
            'title': item.title,
            'link': item.link,
            'publisher': publisher,  # Add publisher to the story dictionary
            'published': published,  # Add published date to the story dictionary
        }
        stories.append(story)
    return stories


# List of keywords for which you want to get stories
keywords = [
    'ESG Supply Chain Management',
    'ESG Logistics',
    'Green Logistics',
    'Carbon Footprint in Supply Chain',
    'Social Responsibility in Supply Chain Management',
    'Sustainable Shipping',
    'Sustainable Freight',
    'Sustainable Transport',
    'Eco-friendly Packaging and Distribution',
    'Environmental Impact of Logistics'
]

# Loop through each keyword, get stories, and save them to a unique Excel file
for i, keyword in enumerate(keywords, start=1):
    stories = get_titles(keyword)
    df_stories = pd.DataFrame(stories)
    excel_path = f'esg_logistics_news{i}.xlsx'  # Create a unique file name for each keyword
    df_stories.to_excel(excel_path, index=False)
    print(f"{len(stories)} stories found and saved to {excel_path}")

