from time import sleep

print("-" * 30)
print("CADASTRE UMA PESSOA")
print("-" * 30)

contM = 0
contF = 0
demaior = 0
demenor = 0

while True:
    idade = int(input("Idade: "))
    sexo = str(input("Sexo (M/F): ")).strip().upper()
    print("")

    if idade >= 18:
        demaior += 1

    if sexo == "M":
        contM += 1
      
    if sexo == "F" and idade < 20:
        contF += 1
        demenor -= 1

    continua = str(input("Quer continuar (S/N) ? ")).strip().upper()
    print("")

    if continua == 'S':
        continue
    if continua == 'N':
        break

print("Processando informações...")
sleep(1.2)
print("")
print(f"Total de pessoas com mais de 18 anos: {demaior}")
print(f"Ao todo temos {contM} homem/homens cadastrados.")
print(f"Temos {contF} mulher com menos de 20 anos.")