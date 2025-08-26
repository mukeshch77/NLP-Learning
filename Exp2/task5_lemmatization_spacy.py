import spacy

text = "The striped bats are hanging on their feet and ate better"
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

for token in doc:
    print(f"{token.text:10} -> {token.lemma_}")
