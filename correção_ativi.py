#main.py

import modulo_ativi as md

def system():
    escolha = input('1 - Verificar notas | 2 para Verificar IMC |  3 para Jogar')
    if escolha  == '1':
        print('Sistema de média')
        lista_notas = []
        quantidade =  int(input('Quantidade de notas: '))
        for i in range(quantidade):
            notas = float(input('notas'))
            lista_notas.append(notas) 
        media = md.sys_notas(lista_notas)
        print('Media notas', media)
    elif escolha == '2':
        print('IMC')
        peso = float(input('Peso: '))
        altura  = float(input('Altura: '))
        imc_usuario = md.imc(peso, altura)
        print(imc_usuario)
    elif escolha == '3':
        print('Jogo de advinhação: ')
        
        md.advinhacao()
    else:
        print('Digite algo válido')        


system()