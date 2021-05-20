import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Add tree species to database. Use web scrapping.'

    def handle(self, *args, **options):
        html_text = requests.get(
            'https://fiszkoteka.pl/zestaw/405991-drzewa-polsko-lacinskie').text
        soup = BeautifulSoup(html_text, 'lxml')
        tr = soup.find_all('tr')
        