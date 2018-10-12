import requests
import json
class Service:
    @staticmethod
    def get_corpus(url):
        corpus = requests.get(url).json()
        return corpus['meaning']
        
        
