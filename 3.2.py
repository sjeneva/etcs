import os
import gensim
import spacy

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")


# Function to preprocess the content of a file
def preprocess_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


# Function to identify key sentences based on topic relevance
def identify_key_sentences(lda_model, document, num_key_sentences=3):
    # Process the document using spaCy
    doc = nlp(document)

    # Tokenize the document
    tokenized_doc = [token.text for token in doc]

    # Create a bag-of-words representation of the document
    bow_doc = lda_model.id2word.doc2bow(tokenized_doc)

    # Get the topic distribution for the document
    doc_topics = lda_model.get_document_topics(bow_doc)

    # Sort topics by relevance to the document
    sorted_topics = sorted(doc_topics, key=lambda x: x[1], reverse=True)

    # Extract key sentences based on topic relevance
    key_sentences = []
    for topic_id, _ in sorted_topics[:num_key_sentences]:
        # Get sentences containing keywords related to the topic
        relevant_sentences = [sent.text for sent in doc.sents if
                              any(word in sent.text.lower() for word, _ in lda_model.show_topic(topic_id, topn=5))]
        key_sentences.extend(relevant_sentences)

    return key_sentences


if __name__ == "__main__":
    # Load the pre-trained LDA model
    lda_model = gensim.models.LdaModel.load("lda_model")

    # Define the directory containing the text files
    input_directory = "'Separated_Files_2.6'"

    # Define the output directory
    output_directory = "'Separated_Files_3.2"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Process each text file in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.txt'):
            input_file_path = os.path.join(input_directory, filename)
            output_file_path = os.path.join(output_directory, f"{filename}_key_sentences.txt")

            # Preprocess the file
            document_text = preprocess_file(input_file_path)

            # Identify key sentences
            key_sentences = identify_key_sentences(lda_model, document_text)

            # Write key sentences to the output file
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                for sentence in key_sentences:
                    output_file.write(sentence + '\n')

            print(f"Key sentences for {filename} written to {output_file_path}")
