cores = {'limpa':'\033[m',
         'roxo': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[31m'
         }
n1 = int(input('{}digite um numero: '.format(cores['roxo'])))
n2 = n1 - 1
n3 = n1 + 1
print('{}analisando o valor {}, seu antecessor eh {} e seu sucessor eh {}'.format(cores['vermelho'],n1, n2, n3))