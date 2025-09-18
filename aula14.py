import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


# import sqlite3 


# c =  sqlite3.connect('nome.db')
# conn = c.cursor()
# c.execute('CREATE TABLE IF NOT EXISTS nome'


url = 'https://bea3853.github.io/PROCESSO_DATA_SCIENCE/'
respo =  requests.get(url)

soup = BeautifulSoup(respo.text, 'html.parser')

# print(soup)

nomes = []
precos = []
avalicoes = []


for produto in soup.find_all('div', class_='produto'):
    nomes.append(produto.find('h2').text)
    precos.append(produto.find('span', class_='preco').text.replace('R$','').replace('.','').replace(',','.')) 
    avalicoes.append(produto.find('span', class_='avaliacao').text)   


print(nomes)
    
# df = pd.DataFrame ({

# 'Modelo':nomes,
# 'Preços':precos,
# 'Avalicão':avalicoes


# })


# # df.to_csv('smartphones.csv')

# df = pd.read_csv('smartphones.csv')
# # print(df)


# # existe dados faltantes
# # print(df.isnull().sum)


# #limpeza -  remover dados duplicados 

# df = df.drop_duplicates()

# print(df[df['Preços'] < 10000]) # filtrar 


# # extrair marca do modelo 

# df['Marca'] = df['Modelo'].str.split().str[0]


# # estatica básica
# print(df.describe())


# # Preço médio por marca
# preco_medio =  df.groupby('Marca')['Preços'].mean()
# print(preco_medio)

# # visualização de dados 

# plt.figure(figsize=(10,6))
# plt.title('DISTRIBUIÇÃO DE PREÇOS')
# plt.hist(df['Preços'], bins = 20 , color='skyblue', edgecolor = 'black')
# plt.xlabel('Preços')
# plt.show()



# # relação de preço e marca 

# plt.figure(figsize=(10,6))
# preco_medio.plot(kind='bar')
# plt.xticks(rotation = 45)
# plt.show()




# plt.figure(figsize=(10,6))
# plt.scatter(df['Preços'],df['Avalicão'])
# plt.title( 'Preço x avaliação')
# plt.show()



# # A:

# # Distribuição de preço:


# # 1k  3k -  maioria

# # Poucos produtos são premium 

# # B

# # Marcas Dominantes:

# # apple tem o preço mais alto 
# # samsumg e xiaome, faixa intermediaria 



# # C Relação  -  preço  X avaliação
# # produtos mais caros em sempre tem as melhores avaliações 
# # boas opçoes de custo beneficio podem ser encontrada na faixa 1500 -  2500


# # ---------------------------------------------------------

# # toma de decisão 

# # recomendações:

# # aumento do estoque para produtos com custo beneficio 
# # promoções estratégicas para com  alta avaliação e preço médio 
# # monitorar concorrtentes para ajustar os preços do iphone 



# # recomendações futuras 

# # aplica ml para prever 


# # print(df)
# # print(precos)
# # print(nomes)
# # print(avalicoes)