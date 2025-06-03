arq = "compras2.txt"

for c in range(1, 3):
    with open(arq, "a") as arquivo:
        r = str(input(f"Digite o {c}o. alimento e sua quantidade: "))
        arquivo.write(r + "\n")
        d = r.replace(",", " ")
for i in range(1, 3):
    with open(arq, "r") as arquivo:
        arquivo.read(d)
    
