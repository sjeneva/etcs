import os
import pandas as pd
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Define paths
directory_path = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics\SNN\1.4_Korea_SNN_사회_extracted_articles'
output_dir = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics\SNN\2.0_Korea_SNN_사회_extracted_articles'
os.makedirs(output_dir, exist_ok=True)

# Create an instance of Okt for tokenization and POS tagging
okt = Okt()

# List of Korean stopwords
korean_stopwords = [
    "는", "은", "이", "가", "을", "를", "의", "에", "에서", "으로", "에게",
    "와", "과", "까지", "부터", "보다", "만", "동안", "또한", "하지만", "그러나",
    "때문에", "그런데", "그리고", "어떻게", "모두", "자신", "누구", "어디", "언제",
    "무엇", "이런", "저런", "이렇게", "저렇게", "했지만", "말하다", "생각하다",
    "하다", "되다", "수", "있다", "없다"
    # Add more stopwords as needed
]

# Define a function to extract nouns from Korean text
def extract_nouns(text):
    # Tokenize and perform POS tagging
    tokens = okt.pos(text)
    # Filter tokens to keep only nouns (tagged as 'Noun')
    nouns = [word for word, pos in tokens if pos == 'Noun']
    # Join the nouns back to a single string
    return ' '.join(nouns)

# Read multiple text files from the directory and create a DataFrame
text_files = os.listdir(directory_path)
texts = []

for file_name in text_files:
    file_path = os.path.join(directory_path, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
        texts.append(text)

# Create a DataFrame with the text data
df = pd.DataFrame({'text_data': texts})

# Remove duplicates and null values
df = df.drop_duplicates()
df = df.dropna()

# Extract nouns from the text data
df['nouns_only'] = df['text_data'].apply(extract_nouns)

# Create a TF-IDF vectorizer and apply it to the nouns_only column
vectorizer = TfidfVectorizer(stop_words=korean_stopwords)
tfidf_matrix = vectorizer.fit_transform(df['nouns_only'])

# Convert the TF-IDF matrix to a DataFrame
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())

# Define the LDA model
lda = LatentDirichletAllocation(n_components=5, random_state=0)  # Adjust `n_components` as needed

# Fit the model on the TF-IDF data
lda.fit(tfidf_matrix)

# Extract topics
topics = lda.components_

# Output the topics and their top words
n_top_words = 10  # Number of top words to display for each topic
feature_names = vectorizer.get_feature_names_out()

# Save topics and their top words to a file
output_file = os.path.join(output_dir, 'topics.txt')

with open(output_file, 'w', encoding='utf-8') as f:
    for topic_idx, topic in enumerate(topics):
        f.write(f"Topic #{topic_idx + 1}:\n")
        top_words = topic.argsort()[:-n_top_words - 1:-1]
        f.write(" ".join([feature_names[i] for i in top_words]) + '\n\n')

# Notify user of completion
print(f"Topics saved to {output_file}")
