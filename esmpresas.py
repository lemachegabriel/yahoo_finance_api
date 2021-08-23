import requests 
from bs4 import BeautifulSoup
import os


SESSION = requests.Session()
HEADER = {"User-Agent": r"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
url = "https://www.infomoney.com.br/cotacoes/empresas-b3/"
data = SESSION.get(url, headers=HEADER)



soup = BeautifulSoup(data.text, 'html.parser')

data = soup.get_text()


arquivo = open("do_not_delete", "w+",1, 'utf-8')
arquivo.write(data)
