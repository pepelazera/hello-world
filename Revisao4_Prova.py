import json
from Revisao_Prova import *

print("\n--- 4. Teste json.load() ---")

with open("meu_arquivo.json", "r", encoding="utf-8") as f:
    dados_lidos_arquivo = json.load(f)

print(f"Dados lidos do arquivo e convertidos para DICIONARIO: {dados_lidos_arquivo}")
print(f"Tipo da variavel: {type(dados_lidos_arquivo)}")

print(f"Preferencia 1: {dados_lidos_arquivo['preferencias'][0]}")