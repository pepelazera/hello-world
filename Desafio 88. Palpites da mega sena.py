from random import randint
from time import sleep

megasena = []
jogos = []

print('-' * 30)
print('     JOGA NA MEGA SENA       ')
print('-' * 30)

quant = int(input('Quantos jogos você quer que eu sorteie ? '))
total = 1
while total <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in megasena:
            megasena.append(num)
            cont += 1
        if cont >= 6:
            break
    megasena.sort()
    jogos.append(megasena[:])
    megasena.clear()
    total += 1
print('')
print('-=' * 3, f'Sorteando {quant} jogos', '-=' * 3)
print('')
sleep(1)

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-' * 5, ' BOA SORTE! ', '-' * 5)