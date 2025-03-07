cores = {'limpa':'\033[m',
         'roxo': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         }

reais = float(input(f'{cores['vermelho']}Qual o valor do produto ? R$ '))
desconto = (reais * 0.95)
#preco = valor mutiplicado por 5% de desconto
print('{}O produto custava R${}, na promocao com desconto de 5% vai custar R${}'.format(cores['verde'], reais, desconto))