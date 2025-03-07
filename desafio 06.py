cores = {'limpa':'\033[m',
         'roxo': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         }
a = int(input('{}Digite um valor: '.format(cores['amarelo'])))
b = (a*2)
c = (a*3)
d = (a**0.5)
print('{}O dobro de {} vale {}'.format(cores['verde'], a, b))
print('{}O triplo de {} eh {}'.format(cores['verde'], a, c))
print('{}A raiz quadrada de {} vale {:.2f}'.format(cores['verde'], a, d))