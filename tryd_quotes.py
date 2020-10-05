import gzip
import pandas as pd

def tryd_quotes(stocks, path='C:\Tryd5\workspace\historico'):
    
    
    df = pd.DataFrame()
    
    # percorre pasta por pasta, abre o arquivo no formato gz e carrega o arquivo no formato csv
    # primeiro separamos as colunas que iremos utilizar (Data, Preço fechamento e Ajuste), em seguida corrigimos o formato
    # da data e definimos essa coluna como index do dataframe.
    # Em seguida adicionamos esses dados ao dataframe DF
    
    for i in stocks:
        with gzip.open('{}\{}/_diario.gz'.format(path,i)) as f:
            dados = pd.read_csv(f, sep=':')
            dados = dados[dados.columns[[0,5,11]]]
            dados.columns = ['Data', 'Preco','Ajuste']
            dados['Data'] = dados['Data'].apply(lambda x: pd.to_datetime(str(x), format='%Y%m%d'))
            dados.index = dados['Data']
            dados[i] = dados['Preco'] / dados['Ajuste']
            dados.drop(['Data','Preco','Ajuste'], inplace=True, axis=1)
            df = df.join(dados, how='outer')
    
    return df