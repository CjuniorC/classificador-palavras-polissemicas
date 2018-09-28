from Tokenizer import Tokenizer
class Corpus():
    @staticmethod
    def generate_train_base(array, token):
        corpus = []
        for sentence in array:
            if 'manga' in sentence.lower() or 'mangas' in sentence.lower():
                corpus.append(Tokenizer.tokenizer_phrase(sentence.split(' '), token))
        return corpus

    @staticmethod
    def join_corpus(corpus1, corpus2):
        for sentence in corpus2:
            corpus1.append(sentence)
        return corpus1

