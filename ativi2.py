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

lista = ['','Dado','Alterar','Somar os valores','Coletar','Localizar um registro']
escolha =  int(input('''
1 - Dado
2 - Alterar
3 - Coletar
4 - Somar                     
5 - Localizar                                                               
'''))


if escolha == 1:
# - Mostra o dado;
    print(lista[escolha])
    print(dados)
    dado = int(input('Insira o indice'))
    print('Dado:', dados[dado])
# - Alterar o dado;
elif escolha == 2:
    print(lista[escolha])
    indice = int(input('Indice'))
    novo_valor = int(input('Novo valor'))
    dados[indice] = novo_valor
    print('Valor alterado - ', dados)
# - Coletando Dados de Experimentos
elif escolha  == 3:
    print(lista[escolha])
    dados.extend([10,2,3])
    print('Coleta novos dados',dados)

# - Analisando a Soma de Dados de Vendas
elif escolha  == 4:
    print(lista[escolha])
    somar_dados = sum(dados)
    print('Soma:', somar_dados)
# - Localizar um Registro no Conjunto de Dados
elif escolha == 5:
    print(lista[escolha])
    dado = int(input('Escolha o dado'))
    valor = dados.index(dado)
    print('Valor localizado na posição', valor)
else:
    print('Digite algo válido')    