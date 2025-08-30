# - ***Desafio 1 Condicionais***
# ***Crie um sistema de e-commerce, onde o usuário possa:***

# - ***cadastrar-se***
# - ***comprar um produto***
# - ***descobrir o valor total***
# - ***pagar***

#Crie um e-commerce com a estrutura de dicionários.

# - Desafio 1 Condicionais

# Crie um sistema de e-commerce, onde o usuário possa:

# - cadastrar-se
dados = {
    'login':input('Login: '),
    'senha':input('Senha: ')
    }

# acesso ao sistema 
senha =  input('Senha de acesso: ')
login = input('Login de acesso: ')

carrinho = []
meus_valores  = []

if senha == dados['senha'] and login == dados['login']:
    print('E-commerce X')
    # - comprar um produto
    produto = ['','a','b','c']
    valores = ['',200.0,65.0,12.0]

    escolha_pedir = input('DESEJA FAZER O PEDIDO? s/n')
    if escolha_pedir == 's':
        prod1   =  int(input('''
        1 - a
        2 - b
        3 - c '''))       
        prod2   =  int(input('''
        1 - a
        2 - b
        3 - c '''))                        
        prod3   =  int(input('''
        1 - a
        2 - b
        3 - c '''))
        carrinho.extend([produto[prod1], produto[prod2], produto[prod3]])
        meus_valores.extend([valores[prod1], valores[prod2], valores[prod3]])
        print('Seus pedidos:')
        print(carrinho)
        print('Total')
        total = sum(meus_valores)
        print('Total da compra -> R$', total)
        pag = ['','pix','paypal','CC', 'CD']
        forma_pag = int(input('''Digite o ID do pag:
                              1 - PIX
                              2 - Paypal
                              3 - CC
                              4 - CD                              
                               '''))
        
        print('Forma de pagamento', pag[forma_pag])
        print('Obrigada volte sempre!')
    else:
        print('Obrigada volte sempre!')    
        
  




else:
    print('Acesso negado!')    







# - descobrir o valor total
# - pagar