import pandas as pd

tabela = pd.read_csv('dados.csv')
total_vendas = tabela['Vendas'].sum()
print(total_vendas)