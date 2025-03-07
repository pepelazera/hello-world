cores = {'limpa':'\033[m',
         'roxo': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         }

a = float(input(f'{cores['vermelho']}Primeira nota do aluno: '))
b = float(input(f'{cores['vermelho']}Segubda nota do aluno: '))
c = (a + b) / 2
# outro jeito pode ser: c = (a/2 + b/2)
print(f'{cores['verde']}a media entre {a} e {b} eh igual a {c}')