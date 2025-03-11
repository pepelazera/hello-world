cores = {'limpa':'\033[m',
         'roxo': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         }

nota1 = float(input(f'{cores['roxo']}Primeira nota: '))
nota2 = float(input(f'{cores['roxo']}Segunda nota: '))
media = float(nota1 + nota2) / 2 

if media < 5:
    print(f'{cores['vermelho']}Tirando {nota1} e {nota2} sua media eh {media}. O aluno esta reprovado')
elif media < 6.9:
    print(f'{cores["amarelo"]}Tirando {nota1} e {nota2} sua media eh {media}. Voce esta de recuperação')
else:
    print(f'{cores["verde"]}Tirando {nota1} e {nota2} sua media eh {media}. Parabens! Voce passou direto!')