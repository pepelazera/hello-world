from random import randint
from time import sleep

lista = []
jogos = []

print('-' * 30)
print('     JOGA NA MEGA SENA       ')
print('-' * 30)

qntd = int(input('Quantos jogos você quer que sorteie ? '))
total = 1
while total <= qntd:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print('')
print('-' * 6, f'Sorteando {qntd} jogos', '-' * 6)
print('')
sleep(1)

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.7)

print('')
print('-' * 5, 'BOA SORTE!', '-' * 5)