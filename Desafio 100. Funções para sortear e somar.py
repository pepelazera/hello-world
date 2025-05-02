from random import randint
def sorteia():
    numeros = list()
    pares = list()
    for n in range(5):
        numaleat = randint(1,10)
        numeros.append(numaleat)
    print(f"Sorteando {len(numeros)} valores digitados: {' '.join(map(str, numeros))}")
    for v in numeros:
        if v % 2 == 0:
            pares.append(v)
    print(f"Somando os valores pares de {numeros}, temos {sum(pares)}.")


sorteia()