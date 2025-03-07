cores = {'limpa':'\033[m',
         'roxo': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         }

dias = int(input(f'{cores['amarelo']}Quantos dias alugados ? '))
km = float(input(f'{cores['amarelo']}Quantos km rodados ? '))
valorfinal = ((60 * dias) + (0.15 * km)) 
print('{}O total a pagar eh de R${:.2f}'.format(cores['verde'], valorfinal))