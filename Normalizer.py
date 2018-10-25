import string
from nltk.corpus import stopwords

class Normalizer():   
    @staticmethod
    def break_corpus(text):
        for simbol in string.punctuation:
            text = text.replace(simbol, '.')
            text = text.replace('\n', '.')
        n_text = ' '.join(word for word in text.split(' ') if word not in stopwords.words('portuguese'))
        print(n_text)
        return n_text.split('.')
        