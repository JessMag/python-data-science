# 2.Com a linguagem python puro, realize o calculo, sem módulos externos ou internos:
# Criando seus próprios módulos

# 1 -FREQUENCIA  =  [1,2,3,6,4]
# 2 - FREQUENCIA  =  [1.5,6.8,9.7,10.6]
# 3 - FREQUENCIA  =  [200,300,500,700,900,400,600]

# 1 - MEÇA A MODA 
# 2 - MEDIANA
# 3 - MÉDIA

FREQUENCIA_1  =  [1,2,3,6,4]
FREQUENCIA_2  =  [1.5,6.8,9.7,10.6]
FREQUENCIA_3  =  [200,300,500,700,900,400,600]

media1 = round(sum(FREQUENCIA_1)/len(FREQUENCIA_1),2)
media2= round(sum(FREQUENCIA_2)/len(FREQUENCIA_2),2)
media3= round(sum(FREQUENCIA_3)/len(FREQUENCIA_3),2)


mediana1 = FREQUENCIA_1[(int(len(FREQUENCIA_1)/2))]
mediana2 = FREQUENCIA_2[(int(len(FREQUENCIA_2)/2))]
mediana3 = FREQUENCIA_3[(int(len(FREQUENCIA_3)/2))]



print(f'''
      média frequencia 1 é: {media1}
      média frequencia 2 é: {media2}
      média frequencia 3 é: {media3}

      mediana frequencia 1 é: {mediana1}
      mediana frequencia 2 é: {mediana2}
      mediana frequencia 3 é: {mediana3}''')

# média frequencia 1 é: 3.2
#       média frequencia 2 é: 7.15
#       média frequencia 3 é: 514.29

#       mediana frequencia 1 é: 3
#       mediana frequencia 2 é: 8.25
#       mediana frequencia 3 é: 700
