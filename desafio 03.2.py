cores = cores = {'limpa':'\033[m',
         'roxo': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[31m'
         }
x = int(input('primeiro numero: '))
y = int(input('segundo numero: '))
s = x + y
print('{}a soma entre {} e {} vale {}'.format(cores['roxo'], x, y, s))
