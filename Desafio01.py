import json
import os

dados = dict()

dados["nome"] = str(input("Digite seu nome: "))
dados["idade"] = int(input("Digite sua idade: "))
dadosdesafio01 = json.dumps(dados, indent=2)
print(dadosdesafio01)

if os.path.exists(dadosdesafio01):
    with open("dadosdesafios.json", "r") as arquivo:
        d = json.loads(dadosdesafio01)
        dadoslidos = json.load(d)
        print(dadoslidos)
else:
    with open("dadosdesafios.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=2) 