cores = {'limpa':'\033[m',
         'roxo': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         }

r= int(input(f'{cores['vermelho']}Quanto dinheiro voce tem na carteira ? '))
d = (r/5.73)
print('{}Com R${} voce pode comprar U${:.2f}'.format(cores['verde'],r, d))