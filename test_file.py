import requests
from bs4 import BeautifulSoup


html_text = requests.get(
    'https://fiszkoteka.pl/zestaw/405991-drzewa-polsko-lacinskie').text
soup = BeautifulSoup(html_text, 'lxml')
div_tag = soup.find_all('div', class_='text')
# print(div_tag[0].text)
for div in div_tag:

    print(div.text)

