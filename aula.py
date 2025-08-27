
# CTRL + DOIS PONTOS (:) =  COMENTAR TUDO
# CTRL  + D  = SELECIONAR ALGO EM MASSA
# CTRL + SHIFT + Z  =  VOLTAR A ALTERAÇÃO


# sinais aritméticos 

print(100 + 5)
print(100 - 5)
print(100 * 5)
print(100 / 5)
print(100 ** 5)
print(100 % 5)
print(100 // 5)

# sinais lógicos

print(100==2)
print(100>2)
print(100<2)
print(100>=2)
print(100<=2)
print(100!=2)


# ---

# DADOS PRIMITIVOS LITERAIS 

# DADO DO TIPO TEXTO
print('TEXTO')

# DADOS BOOLEANOS
print(False)
print(True)

# DADO REAL

print(10.8)
print(5.8)
print(0.2)
print(.0)
print(2.)

# INTEIROS 

print(5)
print(20)
print(30)

# -------

# VARIÁVEIS -  SEMANTICAS, NOME COMPOSTO USAR _, NÃO COMEÇAR COM Nº, 
# NÃO PODE COMEÇAR COM CARACTERES ESPECIAIS 
# dinamica 
# única

dado = 10
print(type(dado))
dado = 20.2
print(type(dado))
dado = True
print(type(dado))
dado =  'Texto'
print(type(dado))
Dado = True
print(type(dado))

DADO = 20
DADO = 30 

print(type(dado))


# ---

# concatenar  = juntar


nome = 'Maria'
idade =  25
print('Olá', nome)

# concatenar 
print('A', nome, 'tem', idade)
print(f'A {nome} tem {idade} ')

# indentação {organizar o código}

print('teste')


#ATIVIDADE

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso/(altura ** 2)
print('seu imc', round(imc))
# dados boleados
abaixo_peso = imc < 18.5
peso_normal = imc >=18.5 and imc <= 24.9
sobrepeso = imc >=25.0 and imc <= 29.9
obesidade = imc >=30.0 and imc <=34.9
print(f'''
baixo peso = {abaixo_peso}
peso_normal = {peso_normal}
sobrepeso = {sobrepeso}
obesidade = {obesidade}
''')



lista_notas  =  [10,9,8.5]
lista_alunos = ['Junior','Pedro','Caio']

somar_notas  = lista_notas[0] + lista_notas[1] +lista_notas[2]
media  =  somar_notas/3
print('MEDIA',round(media,2))
print('aluno', lista_alunos[0],'-', lista_notas[0])
print('aluno', lista_alunos[1],'-', lista_notas[1])
print('aluno', lista_alunos[2],'-', lista_notas[2])