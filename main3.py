import re
import numpy as np
import pandas as pd
from pprint import pprint
import gensim
import gensim.corpora as corpora
from gensim.models import CoherenceModel
from gensim.utils import simple_preprocess
from gensim.models.ldamodel import LdaModel
from gensim import corpora, models
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.datasets import fetch_20newsgroups  # Importing from sklearn
import pyLDAvis.gensim_models as gensimvis
import multiprocessing

def preprocess_data(documents):
    stop_words = stopwords.words('english')
    # Rest of your preprocessing function goes here
    # Tokenize and remove stopwords
    texts = [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in documents]
    return texts

def main():
    # Fetching data
    data = fetch_20newsgroups(remove=('headers', 'footers', 'quotes'))
    documents = data['data']
    processed_texts = preprocess_data(documents)

    # Create Dictionary and Corpus
    id2word = corpora.Dictionary(processed_texts)
    corpus = [id2word.doc2bow(text) for text in processed_texts]

    # Build LDA model
    lda_model = LdaModel(corpus=corpus, id2word=id2word, num_topics=10, random_state=42, passes=10, alpha='auto', per_word_topics=True)
    pprint(lda_model.print_topics())

    # Coherence Model
    coherence_model_lda = CoherenceModel(model=lda_model, texts=processed_texts, dictionary=id2word, coherence='c_v')
    coherence_lda = coherence_model_lda.get_coherence()
    print(f'Coherence Score: {coherence_lda}')

    # Visualizing with pyLDAvis
    vis = gensimvis.prepare(lda_model, corpus, id2word)
    # Further code for visualization (if needed)

if __name__ == '__main__':
    main()
