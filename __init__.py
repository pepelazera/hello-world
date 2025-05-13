cores = {'limpa':'\033[m',
         'roxo': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         }


def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg))
        if entrada.isalpha():
            print(f"{cores["vermelho"]}ERRO! {entrada} é inválido.{cores["limpa"]}")
        else:
            valido = True
            return float(entrada)
    return None