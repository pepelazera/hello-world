import random
soma = 0
vitoria = 0

print("-" * 30)
print("Vamos jogar par ou ímpar!")
print("-" * 30)

while True:
    valor = int(input("Diga um valor: "))
    jogadacomp = random.randint(0, 20)
    soma = valor + jogadacomp
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input("Par ou Ímpar [P/I] ? ")).strip().upper()
    print(f"Você jogou {valor} e o computador jogou {jogadacomp}. Total de {soma}.", end=' ')
    print("DEU PAR" if soma % 2 == 0 else "DEU ÍMPAR" )

    if soma % 2 == 0: 
        resultado = "P"
    else:
        resultado = "I"

    if tipo == resultado:
        print("")
        print("Você ganhou!")
        print("Vamos jogar novamente...")
        vitoria += 1
        print("")
    else:
        print("")
        print("Você perdeu!")
        break

print(f"GAME OVER. Você venceu {vitoria} vez/vezes.")  