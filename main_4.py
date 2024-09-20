from datetime import datetime
import pandas as pd

# Load the combined Excel file into a DataFrame
df = pd.read_excel( r"C:\Users\1234\OneDrive - 인하대학교\바탕 화면\Google/combined_esg_logistics_news.xlsx")

# Function to convert the 'published' string into a 'Month Year' format
def convert_to_month_year(date_str):
    try:
        # Parse the date string to a datetime object
        date_obj = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %Z')
        # Format the datetime object to 'Month Year' string
        return date_obj.strftime('%B %Y')
    except ValueError:
        # In case of a parsing error, return 'Unknown Date'
        return 'Unknown Date'

# Apply the conversion function to the 'published' column
df['published'] = df['published'].apply(convert_to_month_year)

# Show the first few rows of the updated DataFrame to verify the changes
df.head()
