import requests
from bs4 import BeautifulSoup

# List of URLs to scrape
urls = [
    "https://www.dfnionline.com/csr/gebr-heinemann-unifree-duty-free-mars-partner-reduce-logistics-co2-emissions-17-07-2024/&ved=2ahUKEwiKmr-mo9CIAxXrslYBHU16FvoQxfQBegQIBBAC&usg=AOvVaw0x6cqJhvdXS40H2fYN7z3e",
    "https://www.automotivelogistics.media/finished-vehicle-logistics/cosco-shipping-cuts-emissions-on-vehicle-shipments/45858.article&ved=2ahUKEwiKmr-mo9CIAxXrslYBHU16FvoQxfQBegQIABAC&usg=AOvVaw2E5c77XsJpuJR2OijaH0qn",
    "https://sustainablebrands.com/read/circular-economy/reverse-logistics-accelerating-circular-fashion&ved=2ahUKEwi_-PGmo9CIAxWpsFYBHZ15HhIQxfQBegQIBBAC&usg=AOvVaw2v893YOv8HVglkQpqxbf6M",
    # Add other URLs from your list here
]


# Function to extract main text from the webpage
def extract_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting the main content of the article (might need adjustment depending on the site)
        paragraphs = soup.find_all('p')  # Commonly, article text is in <p> tags
        article_text = '\n'.join([para.get_text() for para in paragraphs])

        # Filename based on URL (sanitized)
        filename = url.split("//")[1].split("/")[0].replace('.', '_') + '.txt'

        # Save the article text to a file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(article_text)

        print(f"Saved: {filename}")

    except Exception as e:
        print(f"Error fetching {url}: {e}")


# Loop through URLs and save each article
for url in urls:
    extract_text_from_url(url)
