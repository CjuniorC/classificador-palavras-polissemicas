from templates.Tagger import Tagger
from templates.Corpus import Corpus
from templates.Tokenizer import Tokenizer
from templates.Normalizer import Normalizer
import math
from unidecode import unidecode

class Script:


    @staticmethod
    def execute(frute, clothes):
        corpus = Tagger().tagger_training_corpus()
        t = Tokenizer().generate_tokenizer(corpus)
        frute = unidecode(frute)
        n_corpus = Normalizer().break_corpus(frute)
        n_corpus = Corpus().generate_train_base(n_corpus, t, 'manga', 'mangas')
        n_corpus = Tagger().tagger(n_corpus, 'fruta')
        clothes = unidecode(clothes)
        n_corpus2 = Normalizer().break_corpus(clothes)
        n_corpus2 = Corpus().generate_train_base(n_corpus2, t, 'manga', 'mangas')
        n_corpus2 = Tagger().tagger(n_corpus2, 'roupa')
        train_corpus = Corpus().join_corpus(n_corpus[:math.trunc(len(n_corpus)/2)], n_corpus2[:math.trunc(len(n_corpus)/2)])
        test_corpus = Corpus().join_corpus(n_corpus[math.trunc(len(n_corpus)/2):], n_corpus2[math.trunc(len(n_corpus)/2):])
        t2 = Tokenizer().generate_tokenizer(train_corpus)
        return {'tagger':t2, 'corpus':test_corpus}



    
