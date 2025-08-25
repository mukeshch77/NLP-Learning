import nltk
import spacy
from nltk.tokenize import sent_tokenize

# Download resources
nltk.download('punkt')
nltk.download('punkt_tab')   # fix for new NLTK versions

text = "Artificial Intelligence is transforming the world. NLP is a key part of AI. Machines are learning to understand human language."

# NLTK Sentence Tokenization
nltk_sentences = sent_tokenize(text)
print("NLTK Sentence Tokenization:", nltk_sentences)

# spaCy Sentence Tokenization
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
spacy_sentences = [sent.text for sent in doc.sents]
print("spaCy Sentence Tokenization:", spacy_sentences)

# Compare
print("Same output?:", nltk_sentences == spacy_sentences)
