from flask import Flask, jsonify
from flask_cors import CORS
from script import Script
from Service import Service


frute = Service.get_corpus('https://classificador-18ac0.firebaseapp.com/frute')
clothes = Service.get_corpus('https://classificador-18ac0.firebaseapp.com/clothes')


app = Flask(__name__)
CORS(app)
@app.route('/<sentence>', methods=['GET'])
def classify(sentence):
    tagged_sentence = Script.execute(sentence, frute, clothes);
    return jsonify(tagged_sentence)

if __name__ == '__main__':
    app.run(debug=True)


