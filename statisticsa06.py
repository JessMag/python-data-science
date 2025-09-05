# 3- APÓS APLIQUE COM O MÓDULO STATISTICS DO PYTHON, CRIANDO SEUS PRÓPRIOS MÓDULOS COM O AUXILIO DA BIBLIOTECA STATISTICS:

# Precisa ter 2 arquivos o #main e o #funcoes.

# Utilize funções** -  Crie seu próprio módulo.

import mod_stat as ms

FREQUENCIA_1  =  [1,2,3,6,4]
FREQUENCIA_2  =  [1.5,6.8,9.7,10.6]
FREQUENCIA_3  =  [200,300,500,700,900,400,600]


print(f'''
      média frequencia 1 é: {ms.media(FREQUENCIA_1)}
      média frequencia 2 é: {ms.media(FREQUENCIA_2)}
      média frequencia 3 é: {ms.media(FREQUENCIA_3)}

      mediana frequencia 1 é: {ms.mediana(FREQUENCIA_1)}
      mediana frequencia 2 é: {ms.mediana(FREQUENCIA_2)}
      mediana frequencia 3 é: {ms.mediana(FREQUENCIA_3)}

      moda frequencia 1 é: {ms.moda(FREQUENCIA_1)}
      moda frequencia 2 é: {ms.moda(FREQUENCIA_2)}
      moda frequencia 3 é: {ms.moda(FREQUENCIA_3)}
      
      ''')