import sqlite3
import tkinter as tk
import pandas as pd


def carregar_db():
    db = sqlite3.connect('meu_banco.db')
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS pessoas(
            vendedor TEXT,
            ano INTEGER,
            vendas REAL       
            
            )
    ''')


    db.commit()
    db.close()


def inserir():

    db = sqlite3.connect('meu_banco.db')
    c = db.cursor()
    vendedor = input_vendedor.get()
    ano = input_ano.get()
    venda = input_venda.get()

    c.execute('INSERT INTO pessoas(vendedor, ano, vendas) VALUES ', vendedor,ano,venda) 
    db.commit()
    db.close()

# df = pd.read_sql_query('meu_banco.db')

    

root = tk.Tk()

root.geometry('500x500')

text = tk.Label(root,text ='Insira os dados', font=(12))
text.grid()

sesao = tk.Frame(root)
sesao.grid(padx=20, pady=30)

text1 = tk.Label(sesao,text = 'Vendedor', font=(12))
text1.grid(row = 0, column=0)
input_vendedor = tk.Entry(sesao, font=(12))
input_vendedor.grid(row= 0, column=1, pady=10)

text2 = tk.Label(sesao,text ='Venda', font=(12))
text2.grid(row=1, column=0)
input_venda = tk.Entry(sesao)
input_venda.grid(row=1, column=1, pady=10)

text3 = tk.Label(sesao,text ='ano', font=(12))
text3.grid(row=2, column=0)
input_ano = tk.Entry(sesao)
input_ano.grid(row=2, column=1,pady=10)

sesao2 = tk.Frame(root)
sesao2.grid(padx=20, pady=30)

btn = tk.Buttin()





root.mainloop()