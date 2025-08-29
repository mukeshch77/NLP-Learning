print("1. Lemmatization produced more meaningful results because it returns dictionary words, unlike stemming which chops endings.")
print("2. spaCy handled lemmatization better (e.g., 'ate' -> 'eat', 'better' -> 'well'), while NLTK requires POS tags to improve results.")
print("3. With punctuation, emojis, hashtags (tweets), tokenization differs: spaCy handles them more accurately than NLTK.")
print("4. Lemmatization is slower because it checks grammar + vocabulary rules, while stemming is just rule-based chopping.")
