import re
import requests


def requestcep(cep):
    requisao = requests.get('https://viacep.com.br/ws/85906500/json/')
    print(requisao.json())

text = 'a123b'
lista = re.sub('[^0-9]', '', text)

    
print(lista)
