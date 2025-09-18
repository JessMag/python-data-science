import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://tabelatest.netlify.app/'
respo =  requests.get(url)

soup = BeautifulSoup(respo.text, 'html.parser')

# print(soup)

nome = []
idade = []
cidade = []
email = []

for n in soup.find_all('tbody'):
    nome.append(n.find_all('td'))
    

print(nome)
