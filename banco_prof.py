# banco python loops 



dados_acesso = {'senha':123, 'conta':1}
opercaoes = {1:[50000.0],2:[],3:[]}


opcao_acesso = input('Deseja acessar o sistema? ')
while opcao_acesso == 's':
    senha  =  int(input('Senha: '))
    conta = int(input('Conta: '))
    if senha == dados_acesso['senha'] and conta == dados_acesso['conta']:
       op = int(input('1 - SALDO | 2 - DEPOSITO | 3 - SAQUE | 4 -  SAIR '))
       if op == 1:
           print(opercaoes[1])
           opcao_acesso = input('Continuar? ')
       elif op == 2:
           valor = float(input('Deposito: '))
           dep = [opercaoes[1][0], valor]     
           saldo = sum(dep)
           print('R$', saldo)
           opcao_acesso = input('Continuar? ')
       elif op == 3:
           valor = float(input('Deposito: '))
           saque = opercaoes[1][0] - valor  
           print('R$', saque)
           opcao_acesso = input('Continuar? ')    
       elif op == 4:
           print('Você escolheu sair...')               


else:
    print('Obrigada volte sempre! ')


