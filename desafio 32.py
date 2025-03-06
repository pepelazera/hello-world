from time import sleep
from datetime import date
ano = int(input('Que ano analisar ? Coloque 0 para analisar o ano atual '))
print('')
print('Processando...')
sleep (1.5)
print('')

if ano == 0:
    ano = date.today().year

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'{ano} é um ano bissexto.')

else:
    print(f'{ano} não é um ano bissexto.')