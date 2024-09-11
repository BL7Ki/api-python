import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__) # inicializando o aplicativo, padrao flask

# construindo as funcionalidades
@app.route('/') # decorator do link, ex: /paginainicial. so a barra ja seria a homepage
def paginainicial():
    return 'A API está funcionando'

# se ficar criando varias rotas aqui vai ficar parecendo que ta construindo um site, a diferenca duma api pra um site e que a api so retorna a resposta em json da info
@app.route('/totalvendas') # endpoint da api, onde o usuario recebe de fato a informação
def totalvendas():
    tabela = pd.read_csv('dados.csv')
    total_vendas = tabela['Vendas'].sum()
    resposta = {'totalvendas': total_vendas} # variavel resposta que guarda a info do total de vendas de fato
    return jsonify(resposta) # usar o jsonify para sair do dict do py e transformar de fato em json
    
    #print(total_vendas) isso n vai existir mais, n se retorna print numa api

# rodando api
app.run()
