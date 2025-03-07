cores = {'limpa':'\033[m',
         'roxo': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         }

from math import sqrt 
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('{}A raiz de {} eh igual a {:.2f}'.format(cores['roxo'], num, raiz))