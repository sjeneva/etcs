import spacy
import os

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm")

def preprocess_file(file_path):
    """
    Preprocess the content of a file by filtering out specific parts of speech.
    Retains only nouns, verbs, adjectives, and adverbs.

    Args:
    file_path: Path to the file to be processed.

    Returns:
    A list of cleaned and preprocessed lines from the file.
    """
    cleaned_lines = []
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        doc = nlp(text)
        # Filter tokens based on POS tags and exclude URLs
        tokens = [token.text for token in doc if token.pos_ in ['NOUN', 'VERB', 'ADJ', 'ADV'] and not token.like_url]
        cleaned_line = " ".join(tokens)
        if cleaned_line:  # Ensure the cleaned line is not empty
            cleaned_lines.append(cleaned_line)
    return cleaned_lines

def process_directory(source_directory, result_directory):
    """
    Process all text files in the source directory and save the results in the result directory.
    """
    # Ensure the result directory exists
    if not os.path.exists(result_directory):
        os.makedirs(result_directory)

    for filename in os.listdir(source_directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(source_directory, filename)
            result_file_path = os.path.join(result_directory, filename)

            cleaned_lines = preprocess_file(file_path)

            # Write the preprocessed text to a new file
            with open(result_file_path, 'w', encoding='utf-8') as result_file:
                result_file.write("\n".join(cleaned_lines))

            print(f"Processed and saved: {filename}")

if __name__ == "__main__":
    source_directory = r'2.2345_Korea_KLN_ESG_extracted_articles'
    result_directory = r'2.6_Korea_SNN_ESG_extracted_articles'
    process_directory(source_directory, result_directory)