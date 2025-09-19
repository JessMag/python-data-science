import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd



def mostrar():
    texto = input2.get()
    text2.config(text=texto)


def descricao():
        
    dados  =  pd.read_csv('dados.csv')
    df = pd.DataFrame(dados)

    desc = df.describe()
    text2.config(text = desc)


def grafico_bar():
    
    dados  =  pd.read_csv('dados.csv')
    df = pd.DataFrame(dados)


    fig, grafico = plt.subplots(figsize = (10,6))
    plt.figure(figsize=(10,6))
    grafico.bar(df['cidade'], df['idade'])
    
    canvas  =  FigureCanvasTkAgg(fig, master = janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)



    # plt.grid(True)
    # plt.show()

janela = tk.Tk()
janela.geometry('2150x1700')
janela.configure(bg='white')


text = tk.Label(janela, text = 'ISSO É UM TEXTO', font=(50), pady = 20)
text.pack()

input2  = tk.Entry(janela, font=(60))
input2.pack(pady = 20)


btn = tk.Button(janela, text = 'Grafico Barra', font=(45), command=grafico_bar)
btn.pack(pady=20)


btn2 = tk.Button(janela, text = 'Mostrar texto', font=(45),command=descricao)
btn2.pack(pady=20)

text2 = tk.Label(janela, text = 'Vai aparecer aqui', font=(50), )
text2.pack(pady = 20)





janela.mainloop()    