print("-=" * 10)
print("Gerador de PA")
print("-=" * 10)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro 
cont = 1
totaltermos = 0
quantidadeextra = 10

while quantidadeextra != 0:
    totaltermos = totaltermos + quantidadeextra
    while cont <= totaltermos:
        print(f"{termo} → ", end='')
        termo += razao
        cont += 1
    print("PAUSA")
    quantidadeextra = int(input("Quantos termos a mais você quer mostrar ? "))
print(f"Progressão finalizada com {totaltermos} termos mostrados")
