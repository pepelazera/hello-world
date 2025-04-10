total = []
pares = [] 
impares = []

for n in range(0,7):
     numero = int(input(f'Digite o {n+1}o. valor: '))
     total.append(numero)

for n in total:
    if n % 2 != 0:
      impares.append(n)
    else:
      pares.append(n)

pares.sort()
impares.sort()
print('Os valores pares digitados foram', ', '.join(map(str, pares)))
print('Os valores ímpares digitados foram', ', '.join(map(str, impares)))