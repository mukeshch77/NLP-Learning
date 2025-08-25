from nltk.stem import PorterStemmer

words = ["playing", "played", "plays", "happily", "happiness", "better"]

ps = PorterStemmer()
stemmed_words = [ps.stem(w) for w in words]

print("Original Words:", words)
print("Stemmed Words:", stemmed_words)
