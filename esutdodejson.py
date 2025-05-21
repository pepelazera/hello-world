import json

dicionario = {
    "nome": "Alberto",
    "idade": "22",
    "cidade": "Roma"
}

object_json = json.dumps(dicionario, indent=2)

with open("simples.json", "w") as file:
    file.write(object_json)

print(object_json)