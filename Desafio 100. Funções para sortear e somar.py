from random import randint
numeros = list()

def sorteia(): # Função dos valores gerais
    for n in range(5):
        numaleat = randint(1,10)
        numeros.append(numaleat)
    print(f"Sorteando {len(numeros)} valores digitados: {' '.join(map(str, numeros))}")

def paressoma(): # Função que faz a identificação de valores pares.
    pares = list()
    for v in numeros:
        if v % 2 == 0:
            pares.append(v)
    print(f"Somando os valores pares de {numeros}, temos {sum(pares)}.")

# Programa principal
sorteia()
paressoma()
