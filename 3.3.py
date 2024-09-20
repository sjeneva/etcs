import os
from konlpy.tag import Okt  # Using Okt tokenizer from konlpy
from gensim import corpora, models
from multiprocessing import Pool

# Function to read text from a file
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Directory paths
input_dir = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESGL_Korean\HJ\1_Extracted-Articles_EN_3'
output_dir = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESGL_Korean\HJ\1_Extracted-Articles_EN_4'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Set up Korean tokenizer and stopwords
tokenizer = Okt()
stop_words = set()  # Update this set with your actual stopwords

def process_file(filename):
    file_path = os.path.join(input_dir, filename)
    text = read_text_file(file_path)
    if not text.strip():
        return f"Skipping empty file: {filename}"

    processed_text = tokenizer.morphs(text)
    filtered_text = [word for word in processed_text if word not in stop_words]

    if not filtered_text:
        return f"No tokens after processing for file: {filename}"

    dictionary = corpora.Dictionary([filtered_text])
    corpus = [dictionary.doc2bow(filtered_text)]
    if not corpus:
        return f"Empty corpus for file: {filename}"

    lda_model = models.LdaModel(
        corpus=corpus,
        id2word=dictionary,
        num_topics=2,
        random_state=100,
        update_every=1,
        chunksize=1000,
        passes=1000,
        alpha='auto',
        per_word_topics=True
    )

    output_filepath = os.path.join(output_dir, f'topics_{filename}')
    with open(output_filepath, 'w', encoding='utf-8') as f:
        for idx in range(lda_model.num_topics):
            words_and_probs = lda_model.show_topic(idx, topn=5)
            formatted_topic = ", ".join([f"{word} ({prob:.2f})" for word, prob in words_and_probs])
            f.write(f"Topic {idx}: {formatted_topic}\n")
    return f"Processed {filename}"

if __name__ == '__main__':
    files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]
    with Pool(processes=4) as pool:  # Adjust the number of processes based on your CPU
        results = pool.map(process_file, files)
    for result in results:
        print(result)
