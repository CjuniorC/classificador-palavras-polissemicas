from flask import Flask, jsonify
from flask_cors import CORS
from templates.Script import Script
from templates.Service import Service
from nltk.corpus import stopwords
from templates.Tokenizer import Tokenizer


frute = Service.get_corpus('https://classificador-18ac0.firebaseapp.com/frute')
clothes = Service.get_corpus('https://classificador-18ac0.firebaseapp.com/clothes')
tagger = Script.execute(frute, clothes);


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(Tokenizer().tokenizer_phrase(sentence.split(' '), tagger))
    

# CORS(app)
# @app.route('/<sentence>', methods=['GET'])
# def classify(sentence):
#     # sentence = ' '.join(word for word in sentence.split(' ') if word not in stopwords.words('portuguese'))
#     # tagged_sentence = Script.execute(frute, clothes);
#     # return jsonify(tagged_sentence)

if __name__ == '__main__':
    app.run()


