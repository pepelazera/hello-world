import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)


# Construir as funcionalidades
@app.route("/")  # Diz qual link que irá rodar a função
def homepage():
    return "A API está no ar."


@app.route("/pegarvendas")
def vendas():
    tabela = pd.read_csv("dados.csv")
    total_vendas = tabela["Vendas"].sum()
    resposta = {"total_vendas": total_vendas}
    return jsonify(resposta) # Converter o dicionário para json


# Rodar a nossa api
app.run(host="0.0.0.0")

