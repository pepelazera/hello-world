from random import randint

listaN = (randint(1, 10), randint(1,10), randint(1,10), randint(1, 10), randint(1, 10))

print('Os valores sorteados foram: ', end='')
for n in listaN:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(listaN)}')
print(f'O menor valor sorteado foi {min(listaN)}')