from time import sleep
cores = {'limpa':'\033[m',
         'roxo': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         }

idade2 = 0
idade3 = 0

for count in range(1, 8):
    idade = int(input(f'{cores["amarelo"]}Digite a idade {count}: ')) 
    if idade >= 18:
        idade2 += 1
    else:
        idade3 += 1

print('')
print('Processando informações...')
print('')
sleep(1.4)
print(f'{cores["vermelho"]}Temos {idade3} pessoas de menor e {cores["verde"]}{idade2} pessoas de maior')
