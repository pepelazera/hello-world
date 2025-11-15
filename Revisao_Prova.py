import json

dados = {
    "nome": input("Digite seu nome: "),
    "id": 897,
    "email_verificado": True,
    "preferencias": ["dark mode", "email_diario"],
    "ultimo_acesso": None
}

print("--- 1. Teste json.dumps() ---")

string_json = json.dumps(dados, indent=2) # Transforma um objeto Python em uma String formatada como Json

print(f"\nA variavel 'string_json' agora eh uma STRING: {string_json}")
print(f"Tipo da variavel: {type(string_json)}")


