# - ***Desafio 1 Condicionais***
# ***Crie um sistema de e-commerce, onde o usuário possa:***

# - ***cadastrar-se***
# - ***comprar um produto***
# - ***descobrir o valor total***
# - ***pagar***

#Crie um e-commerce com a estrutura de dicionários.


Produtos = {
    'Livros' : ['abc','cde','efg'],
    'Tablets': ['samsung','lg'],
    'Fone' : ['jbl', 'sony']}


Preços = {
    'Livros': [ 49.99, 19.99, 64.99],
    'Tablets': [450,550],
    'Fone' : [34.99,89.99]}


dados = {}

print('Cadastre-se')

login = input('Digite seu login: ')
senha = int(input('Digite sua senha: '))

dados['login'] = login
dados['senha'] = senha
print('Acesse o sistema')
login_acesso  = input('Digite seu login: ')
senha_acesso = int(input('Digite sua senha: '))
if login_acesso == dados['login'] and senha_acesso == dados['senha']:
    print('Seja bem vindo ao sistema')
    # comprar produto
    # descobrir o valor
    # pagamento
    print(f'''  MEU E-COMMERCE
    ----------------------------------------------------------------------
    Livros:
    ID 0  {Produtos['Livros'][0]} - R$ {Preços["Livros"][0]}
    ID 1 {Produtos['Livros'][1]} - R$ {Preços["Livros"][1]}
    ID 2  {Produtos['Livros'][2]} - R$ {Preços["Livros"][2]}
    Tablets:
    ID 0 {Produtos["Tablets"][0]} - R$ {Preços["Tablets"][0]}
    ID 1 {Produtos["Tablets"][1]} - R$ {Preços["Tablets"][1]}
    Fone:
    ID 0  {Produtos["Fone"][0]} - R$ {Preços["Fone"][0]}
    ID 1  {Produtos["Fone"][1]} - R$ {Preços["Fone"][1]}
    ----------------------------------------------------------------------
''')
    carrinho =[]
    meu_total = []
    secao = input('escolha sua seção: ')
    print (Produtos[secao])
    escolha_1 = int(input('escolha pelo id: '))
    carrinho.append (Produtos[secao][escolha_1])
    meu_total.append (Preços[secao][escolha_1])



    print (f'''
    ----------------------------------------------------------------------
    Seu Carrinho:
    {carrinho}
    {meu_total}


    Total
    {sum (meu_total)}
    ----------------------------------------------------------------------''')

else:
    print('Acesso negado')



mais = input




                 

pagamento = input('qual metodo de pagamento?: ')






# - ***Desafio 2  Condicionais***
# ***Você é um Dev Jr. e precisa criar um sistema de coletas de dados.*** 

# ***Utilize as condicionais, para escolher o tipo de dado e os métodos de lista*** 

# ***para:***

# Exemplo: 

# ***dados = [10,20,30,10]***

# - ***Mostra o dado;***
# - ***Alterar o dado;***
# - ***Coletando Dados de Experimentos***
# - ***Analisando a Soma de Dados de Vendas***
# - ***Localizar um Registro no Conjunto de Dados***


dados = [10,20,30,10]

novo_dado = int(input('insira um novo dado >>>> '))

if novo_dado == int():
    dados.append (novo_dado)
    print (f''' seu dado foi inserido com sucesso:
          {dados} ''')
else:
    print('dado precisa ser numerico inteiro')
