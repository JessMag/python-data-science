import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 

df  =  pd.read_csv('dados.csv')

media  =  df['Vendas'].mean()
print('Media', media)

plt.figure(figsize=(20,8))
sns.lineplot(x='Meses', y='Vendas', marker = 'o',data=df, linewidth = 2.5, color = 'red')
plt.grid(True)
sns.axes_style({"font.family" : "dark", "fontsize":5, 'font.sans-serif': ["Geneva"]})
plt.xticks(rotation= 45)
plt.title('Teste SEABORN')

plt.show()
