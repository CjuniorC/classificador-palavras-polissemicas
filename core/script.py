from Tagger import Tagger
from Corpus import Corpus
from Tokenizer import Tokenizer
from Normalizer import Normalizer

class Script:
    @staticmethod
    def execute(sentence, frute, clothes):
        corpus = Tagger().tagger_training_corpus()
        t = Tokenizer().generate_tokenizer(corpus)
        n_corpus = Normalizer().break_corpus(frute)
        n_corpus = Corpus().generate_train_base(n_corpus, t, 'manga', 'mangas')
        n_corpus = Tagger().tagger(n_corpus, 'fruta')
        n_corpus2 = Normalizer().break_corpus(clothes)
        n_corpus2 = Corpus().generate_train_base(n_corpus2, t, 'manga', 'mangas')
        n_corpus2 = Tagger().tagger(n_corpus2, 'roupa')
        n_corpus = Corpus().join_corpus(n_corpus, n_corpus2)
        t2 = Tokenizer().generate_tokenizer(n_corpus)
        return Tokenizer().tokenizer_phrase(sentence.split(' '), t2);
