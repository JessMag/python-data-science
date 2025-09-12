import pandas as pd 

# 1 - # Lendo o arquivo CSV
dados  =  pd.read_csv('dados.csv')
# 2 - # crie um dataFrame
df =  pd.DataFrame(dados)
# 3 - # calcule a média de idade
media  =  df['Idade'].mean()
print("media", media)
# 4 - # mediana de idade
print('mediana', df['Idade'].median())
# 5 - # busque os dados da Maria 
# print(df.iloc[2])
print(df[df['Nome'] == 'Maria'])
# 6 - # verifique as informações do csv info()
print(df.info())
# 7 - # traga descrição básica
print(df.describe())
# 8 - # agregação com o groupby()
print(df.groupby('Vendas')['Idade'].mean())

['Nome'] == 'Maria'
# 6 - # verifique as informações do csv info()
print(df.info())
# 7 - # traga descrição básica
print(df.describe())
# 8 - # agregação com o groupby()
print(df.groupby('Vendas')['Idade'].mean())

