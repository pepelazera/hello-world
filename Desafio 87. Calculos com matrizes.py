matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matrizpar = []
maiorlinha1 = []

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para {l}, {c}: '))

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

for pares in matriz:
    for num in pares:
        if num % 2 == 0:
            matrizpar.append(num)

somalinha = matriz[0][2], matriz[1][2], matriz[2][2]
print('')
print(f'A soma dos valores pares é {sum(matrizpar)}.')
print(f'A soma dos valores da terceira coluna é {sum(somalinha)}.')
print(f'O maior valor da segunda coluna é {max(matriz[1])}.')