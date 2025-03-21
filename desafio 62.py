print("-=" * 10)
print("Gerador de PA")
print("-=" * 10)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro 
cont = 1

while cont <= 10:
    print(f"{termo} → ", end='')
    termo += razao
    cont += 1
print("PAUSA")

totaltermos = 0

while True:
    quantidadeextra = int(input("Quantos termos a mais você quer mostrar ? "))
    contdois = 1

    while contdois <= quantidadeextra:
        print(f"{termo} → ", end="")
        termo += razao
        contdois += 1
        totaltermos += 1
    print("FIM")

    if quantidadeextra == 0:
        print(f"Paramos aqui. Você utilizou {totaltermos} termos a mais")
        break