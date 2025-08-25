import nltk
import spacy
from nltk.tokenize import word_tokenize

nltk.download('punkt')

text = "Artificial Intelligence is transforming the world. NLP is a key part of AI. Machines are learning to understand human language."

# NLTK Word Tokenization
nltk_words = word_tokenize(text)
print("NLTK Word Tokens:", nltk_words)
print("Unique tokens (NLTK):", len(set(nltk_words)))

# spaCy Word Tokenization
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
spacy_words = [token.text for token in doc]
print("spaCy Word Tokens:", spacy_words)
print("Unique tokens (spaCy):", len(set(spacy_words)))
