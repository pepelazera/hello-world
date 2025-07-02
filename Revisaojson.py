import json

# Converter dicionário para JSON 
dados = {"nome": "Pedro", "idade": 19}
jsonstring = json.dumps(dados, indent=2) # Salva dados Python diretamente em um arquivo JSON. Já o indent formata o JSON com indentação
print(jsonstring)

print("")

# Salvar JSON em um arquivo
with open ("dados.json", "w") as arquivo:
   json.dump(dados, arquivo, indent=2) # Irá criar um arquivo com o nome dentro do parêntese e depois colocar as informações do dicionário dentro dessa pasta em formato JSON

# Ler informações de um arquivo JSON
with open("dados.json", "r") as arquivo:
    dadoslidos = json.load(arquivo) # Load irá carregar as informações do arquivo JSON 
    print(dadoslidos)

print("")

# Converter arquivo JSON para dicionário
texto = '{"nome": "Pedro", "idade":19}'
dados2 = json.loads(texto) # Converte as informações do json para um dicionário para que assim possa se retirar uma informação ou outra, sem puxar o dicionário inteiro
print(dados2["nome"])

print("")
