import pandas as pd
import requests
from bs4 import BeautifulSoup

def load_ibrx100():
    
    ## Carregando a lista dos ativos que compõe o IBRX-100
    req = requests.get('http://br.advfn.com/indice/ibrx')
    if req.status_code == 200:
        print('Requisição bem sucedida!')
        content = req.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find_all(name='table')
    ativos = pd.read_html(str(table))[3]
    pastas = list(ativos['Ativo'])
    
    return pastas