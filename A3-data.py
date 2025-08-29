
# Calcular a média das notas de cada aluno.
# Identificar o aluno com a maior média.
# Calcular a média da classe (média geral de todos)


notas = [[10,10,10],[5,2,3],[5,9,8],[10,0,6]]
nomes = ['Ana','Fernanda', 'Caio', 'Fernando']

# 1
media_ana = sum(notas[0])/len(notas[0])
media_fernanda = sum(notas[1])/len(notas[1])
media_caio = sum(notas[2])/len(notas[2])
media_fernando = sum(notas[3])/len(notas[3])

print(f'''
Media Ana  = {round(media_ana,2)}
Media Fernada = {round(media_fernanda,2)}
Media Caio = {round(media_caio,2)}
Media Fernando = {round(media_fernando,2)}
''')


# 2
media_geral = []
media_geral.extend([media_ana,media_fernanda,media_caio,media_fernando])
maior_media = max(media_geral)
posicao_maior_media = media_geral.index(maior_media)
print('Aluno com a maior média: ', nomes[posicao_maior_media])


# 3

media_classe = sum(media_geral)/len(media_geral)
print('Média da classe: ', media_classe)