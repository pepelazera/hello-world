cores = {'limpa':'\033[m',
         'roxo': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
nome = input(f'{cores['amarelo']}Qual seu nome ? ')
print(f'{cores['roxo']}Seja bem-vindo, {nome}')
