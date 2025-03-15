cores = {'limpa':'\033[m',
         'roxo': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         }

num = int(input('Digite um número: '))
tot = 0

for count in range(1, num + 1):
    if num % count == 0:
        print(f'{cores["verde"]}', end=' ')
        tot += 1
    else: 
        print(f'{cores["vermelho"]}', end=' ')
    print(f'{count}', end=' ')
print(f'\n{cores['limpa']}O número {num} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele É PRIMO', end=' ')
else:
    print('e por isso ele NÃO É PRIMO', end=' ')