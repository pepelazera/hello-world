cores = {'limpa':'\033[m',
         'roxo': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         }


print(f'{cores["amarelo"]}==' * 10)
print(f'{cores["roxo"]}10 termos de uma PA')
print(f'{cores['amarelo']}==' * 10)

primeiro_termo = int(input(f'{cores["roxo"]}Primeiro termo: '))
razão = int(input(f'{cores["roxo"]}Razão: '))
quantidade_termos = 10

print(f'{cores["verde"]}Os termos da PA são: ')
for n in range(1, quantidade_termos + 1):
    pa = primeiro_termo + (n - 1) * razão
    print(pa, end=' → ')
print('ACABOU')