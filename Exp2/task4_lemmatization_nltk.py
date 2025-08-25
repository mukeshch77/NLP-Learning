import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('omw-1.4')

words = ["playing", "played", "plays", "happily", "happiness", "better"]

lemmatizer = WordNetLemmatizer()

print("Default (noun):", [lemmatizer.lemmatize(w) for w in words])
print("As verbs:", [lemmatizer.lemmatize(w, pos='v') for w in words])
print("As adjectives:", [lemmatizer.lemmatize(w, pos='a') for w in words])
