with open("compras.txt", "a") as arquivo:
    for c in range(1,6):
        r = str(input(f"Digite o {c}o. alimento: "))
        arquivo.write(r + "\n")