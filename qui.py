import requests
from bs4 import BeautifulSoup

#  baixa a pag 
url = 'https://bea3853.github.io/PYTHON_PARA_DATA_SCIENCE/'
response = requests.get(url)
html = response.text  # Obtém o conteúdo HTML

#criar o objeto BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# encontrar todas as divs
print("\n=== Todas as divs ===")
todas_divs = soup.find_all('div')

for i, div in enumerate(todas_divs, 1):
    print(f"\nDiv {i}:")
    print("Classes:", div.get('class', ['Nenhuma classe']))
    print("ID:", div.get('id', 'Nenhum ID'))
    print("Conteúdo textual:", div.get_text(strip=True)[:50] + "...")

# Acessando divs específicas (com verificação para evitar NoneType)
print("\n=== Divs específicas ===")
div_header = soup.find('div', class_='header')
if div_header:  # Verifica se encontrou a div
    print("\nCabeçalho:", div_header.get_text(strip=True))
else:
    print("\nDiv header não encontrada")

div_produtos = soup.find('div', class_='produtos')
if div_produtos:
    produtos = div_produtos.find_all('div', class_='produto')
    print("\nProdutos encontrados:", len(produtos))
else:
    print("\nDiv produtos não encontrada")

# div_footer = soup.find('div', class_='footer')
# if div_footer:
#     print("\nRodapé:", div_footer.get_text(strip=True))
# else:
    #   print('Não encontrei')