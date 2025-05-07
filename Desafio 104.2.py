cores = {'limpa':'\033[m',
         'roxo': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         }


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f"{cores["vermelho"]}ERRO! Digite um número inteiro válido.{cores["limpa"]}.")
        if ok:
            break
    return valor


n = leiaInt("Digite um número: ")
print(f"Você digitou o número {n}.")