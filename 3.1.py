import os
from gensim import corpora, models

# Function to preprocess the content of a file
def preprocess_file(file_path):
    cleaned_lines = []
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        cleaned_lines.append(text)
    return cleaned_lines

# Function to process all text files in the source directory
def process_directory(source_directory):
    preprocessed_texts = []
    file_names = []

    for filename in os.listdir(source_directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(source_directory, filename)
            cleaned_lines = preprocess_file(file_path)
            preprocessed_texts.extend(cleaned_lines)
            file_names.append(filename)

    return preprocessed_texts, file_names

# Function to describe topics in a more readable way
def describe_topics(lda_model, doc_topics):
    topic_descriptions = []
    for topic_id, prop in doc_topics:
        # Get top words for this topic
        top_words = lda_model.show_topic(topic_id, topn=5)
        topic_description = f"Topic {topic_id} ({prop:.1%}): " + ', '.join([word for word, _ in top_words])
        topic_descriptions.append(topic_description)
    return ' | '.join(topic_descriptions)

if __name__ == "__main__":
    source_directory = r'Separated_Files_2.6'
    preprocessed_texts, file_names = process_directory(source_directory)

    # Tokenize the preprocessed texts
    tokenized_texts = [text.split() for text in preprocessed_texts]

    # Create a dictionary mapping of words to unique IDs
    dictionary = corpora.Dictionary(tokenized_texts)

    # Convert tokenized texts into a document-term matrix
    corpus = [dictionary.doc2bow(text) for text in tokenized_texts]

    # Train the LDA model
    num_topics = 5
    lda_model = models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=10)

    # Define the output directory
    output_directory = r'Separated_Files_3.1'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Write LDA results to text files
    for idx, topic in lda_model.print_topics(-1):
        with open(os.path.join(output_directory, f"topic_{idx}.txt"), 'w', encoding='utf-8') as file:
            file.write(f'Topic: {idx}\nWords: {topic}\n')

    # Analyze and describe the distribution of topics across documents
    for i, doc in enumerate(corpus):
        doc_topics = lda_model[doc]
        topic_description = describe_topics(lda_model, doc_topics)
        with open(os.path.join(output_directory, f"document_{file_names[i]}_topics.txt"), 'w', encoding='utf-8') as file:
            file.write(f"Document: {file_names[i]}\nTopics: {topic_description}\n")

    print("LDA results saved to directory:", output_directory)