# EXERCICIO 1:

# dados.csv
# Nome,Idade,Cidade
# Ana,25,São Paulo
# João,30,Rio de Janeiro
# Maria,22,Belo Horizonte
# Carlos,35,Porto Alegre

# Crie um csv, e faça um analise baseada nos dados oferecidos.
import pandas as pd

# 1 - # Lendo o arquivo CSV
dados = pd.read_csv('dados.csv')

# 2 - # crie um dataFrame
df = pd.DataFrame(dados)

# 3 - # calcule a média de idade
media = df['Idade'].mean()

# 4 - # mediana de idade
mediana = df['Idade'].median()

# 5 - # busque os dados da Maria 
maria =  df.loc[df['Nome'] == 'Maria']

# 6 - # verifique as informações do csv
inf = df.info()

# 7 - # traga descrição básica
desc = df.describe()

# 8 - # agregação com o groupby
agrega = df.groupby('Cidade')['Idade'].describe()

print(f'''
------------------------------------------
media é {media}
mediana é {mediana}
------------------------------------------
Dados maria
{maria}
------------------------------------------
informações do csv
{inf}
-----------------------------------------
descrição básica
{desc}
-----------------------------------------
descrição básica por cidade
{agrega}
      ''')