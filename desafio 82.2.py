listatot = []
listpares = []
listimpares = []

while True:
    num = int(input('Digite um número: '))
    listatot.append(num)

    if num % 2 == 0:
        listpares.append(num)
    elif num % 2 != 0:
        listimpares.append(num)

    resposta = str(input('Quer continuar ? (S/N): ')).strip().upper()

    if resposta == 'N':
        break

listatot.sort()
print('A lista completa é', ', '.join(map(str, listatot)))
print('A lista dos números pares é', ', '.join(map(str, listpares)))
print('A lista dos números ímpares é', ', '.join(map(str, listimpares))) 