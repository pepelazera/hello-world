arq = "segundoexemplo.txt"

for c in range(1,3):
    with open(arq, "a") as arquivo:
        a = str(input(f"Digite o {c}o. alimento e sua quantidade: "))
        d = a.replace(",", " ").replace(", ", " ")
        arquivo.write(d + "\n")

with open(arq, "r") as arquivo:
    for linha in arquivo:
        print("Você precisa comprar", linha.strip())