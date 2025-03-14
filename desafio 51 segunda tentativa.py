#importações
from time import sleep

#decoração
cores = {'limpa':'\033[m',
         'roxo': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         }


#apresentação do programa
print(f'{cores["amarelo"]}=' * 10)
print(f'{cores["roxo"]}Soma dos 10 termos da PA')
print(f'{cores["amarelo"]}=' * 10)

#introdução dos valores
print('')
primeiro_termo = int(input(f'{cores["roxo"]}Digite o valor do primeiro termo: '))
razão = int(input(f'{cores["roxo"]}Digite o valor da razão: '))
ntermos = 10

#organização do código
print('')
print(f'{cores["verde"]}A soma dos termos dessa PA será: ')
print('')
sleep(0.5)
print(f'{cores["verde"]}Processando...')
sleep(1.4)
print('')

#cálculo da PA
for n in range(1, ntermos + 1):
    pa = primeiro_termo + (n - 1) * razão
    print(pa, end=' → ')
print('ACABOU') 