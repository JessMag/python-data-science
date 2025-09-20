import sqlite3

db = sqlite3.connect('meu_banco.db')

c = db.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS vendas(
          id INTEGER PRIMARY KEY,
          vendedor TEXT,
          ano INTEGER,
          vendas REAL          
        )''')


# vendas = [
#     ('Produto A', 10, 20,450),
#     ('Produto B', 50, 20,60),
#     ('Produto C', 100, 60,30),
#         ]



vendedor1 = ('a','b','c')
ano = (2020,2021,2022)
vendas = (50, 20,60)

c.execute('''
              INSERT INTO vendas (vendedor, ano, vendas) 
              VALUES ('Maria',2021,504540)
              ''')


c.execute('''
              INSERT INTO vendas (vendedor, ano, vendas) 
              VALUES ('Mario',2020,5540)
              ''')





res = c.execute("SELECT id FROM vendas")
dados  = res.fetchall()
for n in dados: 
    print(n)


db.commit()
c.close()

