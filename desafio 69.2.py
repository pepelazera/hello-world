from time import sleep

contM = 0
contF = 0
demaior = 0
demenor = 0

while True:
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input("Sexo (M/F): ")).strip().upper()[0]

    if idade >= 18:
        demaior += 1

    if sexo == "M":
        contM += 1
      
    if sexo == "F" and idade < 20:
        contF += 1
        demenor -= 1

    resp = ' '
    while resp not in "SN":
        resp = str(input("Quer continuar (S/N) ? ")).strip().upper()[0]

    if resp == 'S':
        continue
    if resp == 'N':
        break
    break

print("")
print("Processando informações...")
sleep(1.2)
print("")
print(f"Total de pessoas com mais de 18 anos: {demaior}")
print(f"Ao todo temos {contM} homem/homens cadastrado/cadastrados.")
print(f"Temos {contF} mulher/mulheres com menos de 20 anos.")