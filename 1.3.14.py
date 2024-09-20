import requests
import html2text
import os

# Ensure there's a directory to store the files
output_dir = "Korea_SNN_환경_extracted_articles"
os.makedirs(output_dir, exist_ok=True)


def extract_specific_part_from_text(text, start_marker, end_marker):
    start_index = text.find(start_marker)
    end_index = text.find(end_marker, start_index) + len(end_marker)
    if start_index != -1 and end_index != -1:
        return text[start_index:end_index]
    return "Content not found."

def extract_text_from_url(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
    full_text = html2text.html2text(response.text)
    specific_part = extract_specific_part_from_text(full_text,  "_닫기_", "기자**")
    return specific_part



base_url = ' https://www.klnews.co.kr/news/articleView.html?idxno='
article_partial_urls = [



]

for idx, partial_url in enumerate(article_partial_urls, start=1):
    full_url = base_url + partial_url
    print(f"Extracting content from: {full_url}")
    try:
        article_text = extract_text_from_url(full_url)
        # Extract article ID from URL for filename
        article_id = partial_url.split('=')[-1]
        file_path = os.path.join(output_dir, f"article_{article_id}.txt")

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(article_text)

        print(f"Content saved to {file_path}")
        print("\n---\n")
    except Exception as e:
        print(f"Failed to extract content from {full_url}. Error: {e}")
        print("\n---\n")
