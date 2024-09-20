import os
import spacy
from konlpy.tag import Okt

# Load spaCy's English model for tokenization and language processing.
nlp = spacy.load("en_core_web_sm")

# Initialize the Okt tokenizer from konlpy for Korean noun extraction.
okt_tokenizer = Okt()


def read_file(file_path):
    """
    Read the content of a file and return it as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def tokenize_text(text):
    """
    Tokenize the text using spaCy into sentences.
    """
    doc = nlp(text)
    return [sent.text for sent in doc.sents]


def remove_duplicates(lines):
    """
    Remove duplicate lines from a list of lines.
    """
    return list(set(lines))


def preprocess_sentences(sentences):
    """
    Preprocess sentences by filtering out specific parts of speech (POS).
    Only keep nouns, verbs, adjectives, and adverbs.
    Remove stopwords and irrelevant content such as numbers and punctuation.
    """
    preprocessed_sentences = []
    for sentence in sentences:
        doc = nlp(sentence)
        filtered_tokens = []

        for token in doc:
            # Keep only certain POS tags and exclude stopwords
            if token.pos_ in ['NOUN', 'VERB', 'ADJ', 'ADV'] and not token.is_stop:
                # Optionally filter irrelevant content such as numbers and punctuation
                if token.is_punct or token.like_num:
                    continue
                filtered_tokens.append(token.text)

        # Join the filtered tokens to form the cleaned sentence
        cleaned_sentence = " ".join(filtered_tokens)
        if cleaned_sentence:
            preprocessed_sentences.append(cleaned_sentence)

    return preprocessed_sentences


def extract_nouns(text):
    """
    Extract nouns from a text using Okt tokenizer and filter out one-letter nouns.
    """
    nouns = okt_tokenizer.nouns(text)
    return [noun for noun in nouns if len(noun) > 1]


def process_files(source_directory, result_directory):
    """
    Process files: read, tokenize, remove duplicates, preprocess, and save the results.
    """
    # Ensure the result directory exists
    if not os.path.exists(result_directory):
        os.makedirs(result_directory)

    for filename in os.listdir(source_directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(source_directory, filename)

            # Step 1: Read the file content
            text = read_file(file_path)

            # Step 2: Tokenize text into sentences
            sentences = tokenize_text(text)

            # Step 3: Remove duplicates from the list of sentences
            unique_sentences = remove_duplicates(sentences)

            # Step 4: Preprocess the sentences
            preprocessed_sentences = preprocess_sentences(unique_sentences)

            # Step 5: Extract nouns and filter out one-letter nouns
            nouns = extract_nouns(text)
            filtered_nouns = [noun for noun in nouns if len(noun) > 1]

            # Combine preprocessed sentences and filtered nouns
            cleaned_text = "\n".join(preprocessed_sentences) + "\n" + "\n".join(filtered_nouns)

            # Step 6: Save the cleaned and processed text to the result directory
            result_file_path = os.path.join(result_directory, filename)
            with open(result_file_path, 'w', encoding='utf-8') as result_file:
                result_file.write(cleaned_text)

            print(f"Processed and saved: {filename}")


if __name__ == "__main__":
    # Specify your source and result directories.
    source_directory = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics\SNN\1.4_Korea_SNN_사회_extracted_articles'
    result_directory = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics\SNN\2_Korea_SNN_사회_extracted_articles'

    # Process files from the source directory and save the results to the result directory
    process_files(source_directory, result_directory)
