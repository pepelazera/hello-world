from time import sleep

try:
    num1 = int(input('Primeiro valor: '))
    num2 = int(input('Segundo valor: '))
    num3 = int(input('terceiro valor: '))

except ValueError:
    print("Por favor, insira apenas números inteiros.")
    exit()

# Determina o maior número
maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

# Determine o menor numero
menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

# Resultados
print('')
print('Processando...')
sleep(1.2)
print('')
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')