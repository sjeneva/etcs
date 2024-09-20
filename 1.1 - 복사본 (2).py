from pygooglenews import GoogleNews
import pandas as pd
from datetime import datetime

# Function to get titles
def get_titles(search):
    gn = GoogleNews(lang='en', country='IN')  # English language, India
    stories = []
    search_result = gn.search(search)
    newsitem = search_result['entries']
    for item in newsitem:
        published = item.get('published', 'Unknown Date')
        publisher = item.get('source', {}).get('title', 'Unknown Publisher')
        story = {
            'title': item.title,
            'link': item.link,
            'publisher': publisher,
            'published': published,
        }
        stories.append(story)
    return stories

# Function to convert the 'published' string into a 'Month Year' format
def convert_to_month_year(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %Z')
        return date_obj.strftime('%B %Y')
    except ValueError:
        return 'Unknown Date'

# Keywords list (add your keywords here)
keywords = [
    "ESG Supply Chain Management",
    "ESG Logistics",
    "Green Logistics",
    "SCM Carbon Footprint",
    "SCM Social Responsibility",
    "Sustainable Delivery",
    "Sustainable Transportation Means",
    "Eco-friendly Packaging and Distribution",
    "Environmental Impact of Logistics",
    "ESG Distribution",
    "Sustainable Supply Chain Innovation",
    "Sustainable Logistics Strategy",
    "Renewable Energy-based Logistics",
    "Sustainable Supply Chain Technology Adoption",
    "Environmentally Friendly Logistics Solution Development",
    "SCM Execution in a Circular Economy",
    "ESG-based Logistics Performance Evaluation",
    "Sustainable Inventory Management Strategies",
    "Carbon Neutral Supply Chain Construction",
    "Improvement of Distribution through Eco-labeling",
    "Integration of Social Responsibility and SCM",
    "Energy Efficient Warehouse Operation",
    "Utilization of Eco-friendly Logistics Platforms",
    "Sustainable Procurement Management Strategy",
    "Enhancement of Biodiversity in the Logistics Sector",
    "Sustainable Transportation Network Design",
    "Packaging Techniques for Reducing Environmental Impact",
    "ESG Data Management and Reporting System",
    "Energy Optimization within the Supply Chain",
    "Sustainable Logistics Partnership Construction",
    "Green SCM Policy and Implementation",
    "Education and Awareness for Sustainable Supply Chain",
    "Utilization of Recyclable Materials",
    "Sustainable Supply Chain Finance",
    "Energy-saving Logistics System",
    "Greenhouse Gas Reduction in Logistics Processes",
    "Creation of Social Value and SCM",
    "Ethical Supply Chain Management",
    "Collaborative Logistics with the Local Community",
    "Supply Chain Design for Ecosystem Protection",
    "Waste Management and Reduction Strategies",
    "Renewable Packaging Solutions",
    "Social Distancing Strategies in the Supply Chain",
    "Digital Transformation of the Logistics Sector",
    "Sustainable Supply Chain with AI and Big Data",
    "Smart Logistics and Sustainability",
    "Transport Efficiency Improvement",
    "Biofuel-based Transportation",
    "Supply Chain Risk Management and Sustainability",
    "Green Certification and Standard Compliance",
    "Sustainable Supply Chain Benchmarking",
    "Improvement of Productivity through Eco-friendly Technology",
    "Optimization of Water Use in the Supply Chain",
    "Sustainable Supply Chain Consulting Services",
    "Supply Chain Strategy for Climate Change Response",
    "Sustainable Leadership in the Logistics Sector",
    "Sustainable Supply Chain Audit and Evaluation",
    "Reusable Logistics Resources",
    "Inclusivity and Diversity within the Supply Chain",
    "Sustainable Development of Local Supply Chains",
    ]

all_stories = []  # Initialize an empty list to hold all stories from all searches

# Collect stories for each keyword
for keyword in keywords:
    stories = get_titles(keyword)
    all_stories.extend(stories)  # Extend the list with the new stories

# Convert the list of all stories to a DataFrame
df_all_stories = pd.DataFrame(all_stories)

# Apply the conversion function to the 'published' column
df_all_stories['published'] = df_all_stories['published'].apply(convert_to_month_year)

# Save the DataFrame to an Excel file
excel_path = 'combined_esg_logistics_news.xlsx'
df_all_stories.to_excel(excel_path, index=False)

print(f"All stories saved to {excel_path}")