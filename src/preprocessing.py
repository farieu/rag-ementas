import nltk
from nltk.tokenize import word_tokenize
from rank_bm25 import BM25Okapi

nltk.download("punkt", quiet=True)

def tokenizar_paragrafos(paragrafos):
    return [word_tokenize(p.lower()) for p in paragrafos]

def configurar_bm25(tokenizados):
    return BM25Okapi(tokenizados)