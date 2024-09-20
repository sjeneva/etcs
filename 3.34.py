import re

def split_into_sentences(text):
    """
    Splits the input text into individual sentences and returns them as a list.
    """
    # Split text into sentences using regular expression
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', text)
    return sentences

# Example text to be split into sentences
text_example = """
In literature, distinct frameworks have been proposed for the investigation of big-data problems and issues associated with the supply chain. Hazen et al. (2014) have determined the problems associated with the quality of data in the field of supply chain management. Novel procedures for the monitoring and the managing of data quality have been suggested. The importance of the quality of data in the application and further research in the field of supply chain management has been mentioned. Vera-Baquero ...
"""

# Splitting the example text into sentences
split_sentences = split_into_sentences(text_example)
for i, sentence in enumerate(split_sentences, 1):
    print(f"{i}. {sentence}")

