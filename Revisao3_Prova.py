import json
from Revisao_Prova import *

print("\n---3. Teste json.dump() ---")

with open("meu_arquivo.json", "w") as f:
    json.dump(dados, f, indent=4)

print("Arquivo 'meu_arquivo.json' foi criado/atualizado! ")