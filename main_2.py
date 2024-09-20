# First, you need to install the required packages if you haven't already:
# pip install pygooglenews pandas openpyxl

from pygooglenews import GoogleNews
from datetime import datetime, timedelta
import pandas as pd

# Initialize GoogleNews
gn = GoogleNews(country='USA')

def get_titles(search):
    stories = []
    search_result = gn.search(search)
    newsitem = search_result['entries']
    for item in newsitem:
        story = {
            'title': item.title,
            'link': item.link
        }
        stories.append(story)
    return stories

# Use the function to get stories for 'ESG Logistics'
stories = get_titles('ESG Supply Chain Mangement')
stories = get_titles('ESG Logistics')
stories = get_titles('Green Logistics')
stories = get_titles('Carbon Footprint in Supply Chain')
stories = get_titles('Social Responsibility in Supply Chain Management')
stories = get_titles('Sustainable Shipping')
stories = get_titles('Sustainable Freight')
stories = get_titles('Sustainable Transport')
stories = get_titles('Eco-friendly Packaging and Distribution')
stories = get_titles('Environmental Impact of Logistics')

# Convert the stories to a pandas DataFrame
df_stories = pd.DataFrame(stories)

# Specify the path where you want to save the Excel file
# Change 'your_path_here' to your desired path
excel_path = 'esg_logistics_news1.xlsx'
excel_path = 'esg_logistics_news2.xlsx'
excel_path = 'esg_logistics_news3.xlsx'
excel_path = 'esg_logistics_news4.xlsx'
excel_path = 'esg_logistics_news5.xlsx'
excel_path = 'esg_logistics_news6.xlsx'
excel_path = 'esg_logistics_news7.xlsx'
excel_path = 'esg_logistics_news8.xlsx'
excel_path = 'esg_logistics_news9.xlsx'
excel_path = 'esg_logistics_news10.xlsx'

# Save the DataFrame to an Excel file
df_stories.to_excel(excel_path, index=False)

print(f"{len(stories)} stories found and saved to {excel_path}")
