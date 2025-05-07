def ajuda(com):
    print('')
    help(com)


def titulo(msg):
    tam = len(msg)
    print('-'*tam)
    print(msg)
    print('-'*tam)


# Programa principal
comando = ''
while True:
    titulo("SISTEMA DE AJUDA PyHELP")
    comando = str(input("Função ou Biblioteca: "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
print('Por hoje é só. Muito obrigado!')