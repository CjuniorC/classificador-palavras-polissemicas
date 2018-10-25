from script import Script
from Service import Service
from Normalizer import Normalizer


frute = Service.get_corpus('https://classificador-18ac0.firebaseapp.com/frute')
clothes = Service.get_corpus('https://classificador-18ac0.firebaseapp.com/clothes')

print(Script.execute('Vou comprar uma camisa de manga comprida', frute, clothes))
