def lernomes():
    with open("nomes.txt", "r") as arquivo:
       linhas = [linha.strip() for linha in arquivo.readlines()]
    nome = sorted(linhas)
    return nome

# Programa principal
nomes = lernomes()
print('\n'.join(nomes))