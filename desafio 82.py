lista = []
listaimpar = []
listapar = []

while True: 
    num = (int(input('Digite um valor: ')))
    lista.append(num)
    resposta = str(input('Quer continuar ? (S/N): ')).strip().upper()
    
    if num % 2 != 0:
        listaimpar.append(num)
    if num % 2 == 0:
        listapar.append(num)
    if resposta in 'Nn':
        break

lista.sort()
print('A lista completa é', ', '.join(map(str, lista)))
print('A lista de números ímpares é', ', '.join(map(str, listaimpar)))
print('A lista de números pares é', ', '.join(map(str, listapar)))