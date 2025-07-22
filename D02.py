def leia_nome():
    with open("nomes.txt", "r") as arquivo:
        a = arquivo.readlines()
        a2 = []
        for linha in a:
            if linha.strip() != "":
                a2.append(linha.strip())
        a3 = sorted(a2)
    return a3

# Programa principal
nome = leia_nome()
print('\n'.join(nome))