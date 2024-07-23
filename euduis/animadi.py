import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Tokenize sentences
tokenized_sentences = [nlp(sentence) for sentence in sentences]
tokens = [[token.text for token in doc] for doc in tokenized_sentences]
