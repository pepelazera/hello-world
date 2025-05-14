cores = {'limpa':'\033[m',
         'roxo': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         }


while True:
    try:
        i = int(input("Digite um número inteiro: "))
        r = float(input("Digite um número real: "))
    except (ValueError, TypeError):
        print(f"{cores["vermelho"]}ERRO: por favor, digite um valor válido.{cores["limpa"]}")
    except KeyboardInterrupt:
        print(f"{cores["vermelho"]}ERRO: o usuário encerrou o programa.{cores["limpa"]}")
        break
    else:
        print(f"O valor inteiro digitado foi {i} e o valor real digitado foi {r}.")
        break
