import pandas as pd
import requests
from bs4 import BeautifulSoup

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def load_ibrx100():
    
    ## Carregando a lista dos ativos que compõe o IBRX-100
    req = requests.get('http://br.advfn.com/indice/ibrx', headers=HEADERS)
    if req.status_code == 200:
        print('Requisição bem sucedida!')
        content = req.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find_all(name='table')
    ativos = pd.read_html(str(table))[3]
    pastas = list(ativos['Ativo'])
    
    return pastas
