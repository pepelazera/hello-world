cores = {'limpa':'\033[m',
         'roxo': '\033[7;30;45m',
         'amarelo':'\033[;33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[0;30;41m',
         'verde':'\033[0;30;42m',
         'azul':'\033[0;34;40m',
         'branco':'\033[0;30;47m'
         }


def ajuda(com):
    print('')
    print(f"{cores['azul']}")
    help(com)


def titulo(msg):
    print(f"{cores['roxo']}")
    tam = len(msg)
    print('-'*tam)
    print(msg)
    print('-'*tam)
    print(f"{cores['limpa']}")


# Programa principal
comando = ''
while True:
    titulo("SISTEMA DE AJUDA PyHELP")
    comando = str(input(f"{cores['azul']}Função ou Biblioteca: "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
print('')
print(f"{cores['roxo']}Por hoje é só. Muito obrigado!")