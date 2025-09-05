# modulo.py

import random

def sys_notas(lista_notas):
    media  =  sum(lista_notas)/len(lista_notas)
    return media

def imc(peso, altura):
        return peso / (altura ** 2)

def advinhacao():
    
    for i in range(3,0,-1):
        valor_ale = random.randint(1,20)
        print('Você tem apenas: ', i, 'chances')
        valor  =  int(input('Digite o chute: '))
        if valor_ale == valor:
            
            print('Ganhou o jogo, o valor é,  ', valor_ale)
            break
        else:
            
            print('erro, o valor é: ', valor_ale)
    else:
        print('Perdeu o jogo')