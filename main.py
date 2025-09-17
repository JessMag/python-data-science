from bs4 import BeautifulSoup
import requests

url = "https://bea3853.github.io/meu.site.scraping/"
requi = requests.get (url)
soup = BeautifulSoup (requi.text, 'html.parser')

total_divs = soup.find_all('div')
# print(total_divs)

for i,div in enumerate(total_divs,1):
    print('div',i)
    print('classe', div.get('class',['não tem']))
    print('id', div.get('id','não tem'))
    print('texto', div.get_text(strip=True))