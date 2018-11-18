from flask import Flask, jsonify
from flask_cors import CORS
from templates.Script import Script
from templates.Service import Service
from nltk.corpus import stopwords
from templates.Tagger import Tagger
from templates.Corpus import Corpus
from templates.Tokenizer import Tokenizer
from templates.Normalizer import Normalizer
import nltk
from  unidecode import unidecode

app = Flask(__name__)

tagger = ''
frute = ''
clothes = ''
corpus = ''

CORS(app)
@app.route('/tag/<sentence>', methods=['GET'])
def index(sentence):
    global tagger
    sentence = unidecode(sentence)
    sentence = ' '.join(word for word in sentence.split(' ') if word not in stopwords.words('portuguese'))
    return jsonify(Tokenizer().tokenizer_phrase(sentence.split(' '), tagger))

@app.route('/setup')
def setup():
    global tagger
    global corpus
    frute = Service.get_corpus('https://classificador-18ac0.firebaseapp.com/frute')
    clothes = Service.get_corpus('https://classificador-18ac0.firebaseapp.com/clothes')
    obj = Script.execute(frute, clothes)
    tagger = obj['tagger']
    corpus = obj['corpus']
    return 'ok'

CORS(app)
@app.route('/metrics/words', methods=['GET'])
def words():
    global tagger
    global corpus
    total = sum(len(sentence) for sentence in corpus)
    return jsonify(total)

CORS(app)
@app.route('/metrics/accuracy', methods=['GET'])
def accuracy():
    global tagger
    global corpus
    return jsonify(nltk.BigramTagger.evaluate(tagger, corpus));
   

CORS(app)
@app.route('/metrics/sentences', methods=['GET'])
def sentences():
    global tagger
    global corpus
    return jsonify(len(corpus) * 2)

if __name__ == '__main__':
    app.run()


