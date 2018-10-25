import string
from nltk.corpus import floresta
from nltk.corpus import stopwords
import nltk


class Tagger():

    
    @staticmethod
    def tagger(corpus, tag):
        for sentence in corpus:
            for t in sentence:
                if t[0].lower() == 'manga' or t[0].lower() == 'mangas':
                    pos = sentence.index(t)
                    sentence[pos] = (t[0], '{}+{}'.format((t[1], tag)))
        return corpus

    @staticmethod
    def tagger_training_corpus():
        corpus = []
        for sent in floresta.tagged_sents():
            new_sent = []
            for word in sent:
                if word[0].lower() not in string.punctuation:
                    new_sent.append(word)
            corpus.append(new_sent)
        return corpus