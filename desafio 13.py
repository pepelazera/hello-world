cores = {'limpa':'\033[m',
         'roxo': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         }

salario = float(input(f'{cores['vermelho']}Qual o salario do funcionario ? R$'))
aumento = (salario * 0.15)+(salario)
print ('{}Um funcionario ganhava R${}, com o aument de 15%, passa a receber R${}'.format(cores['verde'], salario, aumento))