import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('mtplt.csv')
df['Valor_Total'] = df['Quantidade'] * df['Preço']

# vendas por categoria 

plt.figure(figsize=(10,15))
vendas_por_categoria = df.groupby('Categoria')['Valor_Total'].sum() 
vendas_por_categoria.plot(kind='bar', color = 'orange')
vendas_por_categoria.plot(kind='line')
plt.title('VENDA POR CATEGORIA')
plt.xlabel('CATEGORIA')
plt.ylabel('VENDA TOTAL')
plt.grid(True)
plt.xticks(rotation = 45)
plt.show()

plt.figure(figsize=(8,8))
vendas_regiao = df.groupby('Região')['Valor_Total'].sum()
colors = ['black','green','yellow', 'red']
vendas_regiao.plot(kind='pie',autopct='%1.1f%%', colors=colors)
plt.title('Valor total por região')
plt.show()

plt.figure(figsize=(8,7))
vendas_produto = df.groupby('Produto')['Valor_Total'].sum()
vendas_produto.plot(kind='hist', bins =25)
plt.show()
