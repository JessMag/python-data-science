import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd



# Ler o arquivo CSV usando Pandas.
data = pd.read_csv('dados_atividade.csv')
df = pd.DataFrame(data)

def grafico_bar():
    data = pd.read_csv('dados_atividade.csv')
    df = pd.DataFrame(data)

    fig, grafico = plt.subplots(figsize = (10,6))
    plt.figure(figsize=(10,6))
    grafico.bar(df['vendedor'], df['vendas'])
    
    canvas  =  FigureCanvasTkAgg(fig, master = janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

def descricao():
    data = pd.read_csv('dados_atividade.csv')
    df = pd.DataFrame(data)

    desc = df.describe()
    text2.config(text = desc)


# Gerar gráficos usando Matplotlib.


# Exibir a interface gráfica com Tkinter.
# Crie 5 botões
# Em cada botão precisa mostrar um tipo de grafico
# Mostre a estatistica também

janela = tk.Tk()
janela.geometry('2150x1700')
janela.configure(bg='skyblue')


text = tk.Label(janela, text = 'ATIVIDADE AULA 15', font=(50))
text.pack(pady = 20)

btn = tk.Button(janela, text = 'Grafico Barra', font=(45),command=grafico_bar)
btn.pack(pady=20)

btn2 = tk.Button(janela, text = 'Grafico Linha', font=(45))
btn2.pack(pady=20)

btn3 = tk.Button(janela, text = 'Histograma', font=(45))
btn3.pack(pady=20)

btn4 = tk.Button(janela, text = 'Grafico Pizza', font=(45))
btn4.pack(pady=20)

btn5 = tk.Button(janela, text = 'Grafico ns', font=(45))
btn5.pack(pady=20)

btn6 = tk.Button(janela, text = 'Mostrar estatistica', font=(45),command=descricao)
btn6.pack(pady=20)

text2 = tk.Label(janela, font=(50),bg='skyblue' )
text2.pack(pady = 20)





janela.mainloop()    