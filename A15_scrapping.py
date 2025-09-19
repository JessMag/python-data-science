import requests
from bs4 import BeautifulSoup
import pandas as pd



url = 'https://tabelatest.netlify.app/'
resp = requests.get(url)
sopa = BeautifulSoup(resp.text, 'html.parser')

c = []

for linha in sopa.find_all('tr')[1:]:
    for n in linha.find_all('td')[1]:
        c.append(int(n))
print(c)


nomes = [linha.find_all('td')[0].text for linha in sopa.find_all('tr')[1:]]
idade = [int(linha.find_all('td')[1].text) for linha in sopa.find_all('tr')[1:]]
cidade = [linha.find_all('td')[2].text for linha in sopa.find_all('tr')[1:]]
e_mail = [linha.find_all('td')[3].text for linha in sopa.find_all('tr')[1:]]
# numeros_idade_inteiros =  [int(n) for n in idade]


df = pd.DataFrame({
'nomes':nomes,
'idade':idade,
'cidade':cidade,
'emails':e_mail, 

})




df.to_html('dados.html')

    

print(idade)
print(nomes)
print(cidade)
print(e_mail)





