from time import sleep
cores = {'limpa':'\033[m',
         'roxo': '\033[7;30;45m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[0;30;41m',
         'verde':'\033[0;30;42m',
         'azul':'\033[0;30;45m'
         }


def ajuda(com):
    print(f"{cores['limpa']}")
    titulo(f"{cores['pretoebranco']}Acessando o manual do comando {com}...")
    print(f"{cores['azul']}", end='')
    help(com)
    sleep(0.5)

def titulo(msg, cor = 0):
    tam = len(msg)
    print(f"{cores['pretoebranco']}", end='')
    print('-'*tam)
    print(f"{msg}")
    print('-'*tam)
    print(f"{cores["limpa"]}")
    sleep(0.5)

# Programa principal
comando = ''
while True:
    titulo(f'{cores["roxo"]}SISTEMA DE AJUDA PyHelp')
    comando = str(input(f"{cores["roxo"]}Função ou Biblioteca: "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
print('')
titulo('ATÉ LOGO')