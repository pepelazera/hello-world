print("-" * 30)
print("     LOJA SUPER BARATÃO      ")
print("-" * 30)

total = maiorvalor = menorvalor = 0

while True:

    nomeProdut = str(input("Nome do produto: "))
    preço = float(input("Preço: "))
    total += preço
    menorvalor += 1

    if preço > 1000:
        maiorvalor += 1
        preço == maiorvalor

    resp = ' '
    while resp not in "SN":
        resp = str(input("Quer continuar (S/N) ? ")).strip().upper()[0]

    if resp == "S":
        continue
    if resp == "N":
        break


print(f"O total da compra foi R${total}")
print(f"Temos {maiorvalor} produto/produtos custando mais de R$1000.00")
print(f"O produto mais barato custa R${menorvalor} ")