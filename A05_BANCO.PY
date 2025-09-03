# 1 - Crie um sistema de banco, com as seguintes operações:
# COM LOOPS - CONDICIONAIS  -  VARIÁVEIS -  LISTAS - DICIONÁRIOS. 

# # SISTEMA DE BANCO 

# - Acesso a conta
# (CONDICIONAL COMPARAR) Ver extrato
# (PRINT(SALDO))
# - Fazer um deposito
# (SOMA -  VALOR SALDO + DEPOSITO(FLOAT))
# - Fazer um saque 
# (SUBTRAÇÃO -  SALDO - SAQUE(FLOAT))
# - Sair do sistema 
# (DESPEDIR)

# dados = {
#     'contas': ['1','4567'],
#     'nomes_cliente':['Maria','Joao'],
#     'senhas': ['1','7654'],
#     'saldo': [.0 , 20.0]
# }

contas = ['1','2']
nomes = ['Maria','Joao']
senhas = ['1','2']
saldos = [.0,20.99]

entrada = True

while entrada:
    print ('------------ Bem vindo ao Banco ------------')
    conta_1 = input ('Digite sua conta: =>')
    senha_1 = input ('Digite sua senha: =>')
    ind = contas.index (conta_1)
    if conta_1 in contas and senha_1 in senhas[ind]:
        escolha = input (f'''' Bem vindo(a), {nomes[ind]}
            qual operação deseja fazer?
            1 - Ver Extrato
            2- Fazer deposito
            3 - Fazer saque
            4 - Sair
            >>>>>>>>>>> ''')
        if escolha == '1':
             print (f'''seu saldo é {saldos[ind]}''')
        elif escolha == '2':
             deposito= float(input('Qual valor do deposito? >'))
             valor_em_conta = saldos[ind]
             valor_final = valor_em_conta + deposito
             saldos.__delitem__(ind)
             saldos.insert(ind,valor_final)
             print(f'''Depósito realizado com sucesso!'
                   saldo atual {saldos[ind]}''')
        elif escolha == '3':
             saque = float(input('Qual valor do saque? >'))
             valor_em_conta = saldos[ind]
             valor_final = valor_em_conta - saque
             if valor_final < 0: print('você não possui saldo suficiente')
             else:
                saldos.__delitem__[ind]
                saldos.insert(ind,valor_final)
                print(f'''Saque realizado com sucesso!'
                   saldo atual {saldos[ind]}''')
        elif escolha == '4':
             print ('Obrigada, volte sempre')
             entrada = False
        else: print ('digite uma opção válida')     
    else:
        print ('senha ou conta incorretas, tente novamente')
else:
    pass


enter = input('clique enter para sair')