nomes = "nomes.txt"


try:
    with open(nomes, "a") as arquivo:
        for c in range(0,5):
            msg = str(input(f"Nome {c+1}: "))
            arquivo.write(msg + "\n")
except (ValueError, TypeError):
    print("ERRO: por favor, digite um nome.")
except KeyboardInterrupt:
    print("Programa encerrado.")
else:
    print("Nomes foram salvos com sucesso!\n")

print("")
print("Os nomes salvos foram: ")
with open(nomes, "r") as arquivo:
    nomes = arquivo.readlines()

nomes.sort()
print("".join(map(str, nomes)))