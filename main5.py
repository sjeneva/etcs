import gensim
import gensim.corpora as corpora
from gensim.models.ldamodel import LdaModel
from gensim.utils import simple_preprocess
from nltk.corpus import stopwords
import nltk

# Download NLTK stopwords if not already downloaded
nltk.download('stopwords')

# Sample documents
doc_a = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."
doc_b = "My mother spends a lot of time driving my brother around to baseball practice."
doc_c = "Some health experts suggest that driving may cause increased tension and blood pressure."
doc_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
doc_e = "Health professionals say that brocolli is good for your health."

# Compile documents
doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]

# Tokenize and remove stop words
stop_words = stopwords.words('english')
texts = [[word for word in simple_preprocess(doc) if word not in stop_words] for doc in doc_set]

# Create Dictionary
id2word = corpora.Dictionary(texts)

# Create Corpus
corpus = [id2word.doc2bow(text) for text in texts]

# Build LDA model
lda_model = LdaModel(corpus=corpus, id2word=id2word, num_topics=2, random_state=100, update_every=1, chunksize=100, passes=10, alpha='auto', per_word_topics=True)

# Get the topics
lda_topics = lda_model.print_topics(num_words=4)
print(lda_topics)
