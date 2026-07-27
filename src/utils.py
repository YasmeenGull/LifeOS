import nltk
from nltk.tokenize import word_tokenize


def print_title(title):
    print()
    print("=" * 50)
    print(title)
    print("=" * 50)


def download_nltk():
    nltk.download("punkt")


def tokenize_text(sentence):
    return word_tokenize(sentence)