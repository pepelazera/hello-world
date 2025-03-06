import random
from time import sleep
numero = int(input('Vou pensar em um numero de 0 a 5. Tente advinhar... '))
print('')
print('Processando...')
sleep(2)
print('')
numerosorteado = (0, 1, 2, 3, 4, 5)

if numero == random.choice(numerosorteado):
    print('Voce acertou, parabens!')
else:
    print('Voce errou! Logo, eu venci')