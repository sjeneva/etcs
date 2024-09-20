import pandas as pd
import spacy
import os

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm")

def preprocess_file(file_path, stop_words):
    """
    Preprocess the content of a file by removing nulls, irrelevant content, and stop words.

    Args:
    file_path: Path to the file to be processed.
    stop_words: A set of stop words to be removed.

    Returns:
    A list of cleaned and preprocessed lines from the file.
    """
    cleaned_lines = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:  # Remove nulls
                doc = nlp(line)
                tokens = [token.text for token in doc if not token.is_punct and not token.is_space and not token.text in stop_words]
                cleaned_line = " ".join(tokens)
                if cleaned_line:  # Check if line is not empty after cleaning
                    cleaned_lines.append(cleaned_line)
    return cleaned_lines

def process_directory(source_directory, result_directory):
    """
    Process all text files in the source directory and save the results in the result directory.

    Args:
    source_directory: The directory containing the original text files.
    result_directory: The directory where the preprocessed files will be saved.
    """
    # Ensure the result directory exists
    if not os.path.exists(result_directory):
        os.makedirs(result_directory)

    stop_words = nlp.Defaults.stop_words  # Get spaCy's default English stop words

    for filename in os.listdir(source_directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(source_directory, filename)
            result_file_path = os.path.join(result_directory, filename)

            cleaned_lines = preprocess_file(file_path, stop_words)

            with open(result_file_path, 'w', encoding='utf-8') as result_file:
                result_file.write("\n".join(cleaned_lines))

            print(f"Processed and saved: {filename}")

if __name__ == "__main__":
    source_directory = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics\Separated_Files_2.1'
    result_directory = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics\Separated_Files_2.345'
    process_directory(source_directory, result_directory)

