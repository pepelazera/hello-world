import json
from Revisao_Prova import *

print("\n--- 2. Teste json.loads() ---")

dados_convertidos = json.loads(string_json)

print(f"A string foi convertida de volta para um DICIONARIO: {dados_convertidos}")
print(f"Tipo da variavel: {type(dados_convertidos)}")

print(f"Nome do usuario: {dados_convertidos['nome']}")