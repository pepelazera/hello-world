# Para ler mensagens simples
with open("email.txt", "r") as arquivo:
    email = arquivo.read()
print(email)

# Para ler mensagens maiores e mais complexas
with open("mensagem.txt", "r", encoding="utf-8") as arquivo: # O encoding serve para adicionar caractéres especiais
    mensagem = arquivo.readlines()
print(mensagem)
for linha in mensagem:
    if "faturamento" in linha: # Isso faz com que você consiga ler somente uma linha entre várias
        print(linha)

with open("senha.txt", "r") as arquivo:
    senha = arquivo.read()

with open("senha.txt", "w") as arquivo:
    arquivo.write("456789")
