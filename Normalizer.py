import string
class Normalizer():
    @staticmethod
    def break_corpus(text):
        for simbol in string.punctuation:
            text = text.replace(simbol, '.')
            text = text.replace('\n', '')
        return text.split('.')

    
