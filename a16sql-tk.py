import sqlite3
import tkinter as tk

db = sqlite3.connect('meu_db.db')

c = db.cursor()

def carregar_db ():
    c.execute (''' CREATE TABLE IF NOT EXISTS pessoas(
            vendedor TEXT,
            ano INTEGER,
            vendas REAL
            )
        ''')

root = tk.Tk()

root.geometry('500x500')

text = tk.Label(root,'insira os dados')
text.grid()

secao = tk.Frame()
secao.grid()

text1 = tk.Label(secao,text='Vendedor',font=(12))
text1.grid(row=0,column=0)
input_vendedor = tk.Entry(secao)
input_vendedor.grid(row=0,column=1)

text3 = tk.Label(secao,text='Venda',font=(12))
text3.grid(row=2,column=0)
input_venda = tk.Entry(secao)
input_venda.grid(row=2,column=1)

text2 = tk.Label(secao,text='Ano',font=(12))
text2.grid(row=3,column=0)
input_ano = tk.Entry(secao)
input_ano.grid(row=3,column=1)

