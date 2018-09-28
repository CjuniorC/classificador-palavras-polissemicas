from nltk import UnigramTagger
from nltk import DefaultTagger
from nltk import BigramTagger

class Tokenizer():
    @staticmethod
    def generate_tokenizer(corpus):
        test = corpus
        t0 = DefaultTagger("n")
        t1 = UnigramTagger(test, backoff=t0)
        t2 = BigramTagger(test, backoff=t1)
        return t2
    
    @staticmethod
    def tokenizer_phrase(phrase, tagger):
        tag_phrase = tagger.tag(phrase)
        return tag_phrase