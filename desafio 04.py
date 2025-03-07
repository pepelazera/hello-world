cores = {'limpa':'\033[m',
         'roxo': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[31m'
         }
a = input(f'{cores['vermelho']}digite algo: ')
print(f'{cores['roxo']}O tipo primitivo desse valor é', type(a))
print(f'{cores['amarelo']}Só tem espaços ?', a.isspace())
print(f'{cores['roxo']}É um número ?', a.isnumeric())
print(f'{cores['amarelo']}É alfabético ?', a.isalpha())
print(f'{cores['roxo']}É alfanumérico ?', a.isalnum())
print(f'{cores['amarelo']}Está em maiúscula ?', a.isupper())
print(f'{cores['roxo']}Está em minúscula ?', a.islower())
print(f'{cores['amarelo']}Está capitalizada ?', a.istitle())