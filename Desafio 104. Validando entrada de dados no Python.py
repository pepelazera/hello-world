cores = {'limpa':'\033[m',
         'roxo': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         }


def leia_int(num):
    print(f"Você digitou o valor {num}.")


# Programa principal
while True:
    n = str(input(f"{cores['limpa']}Digite um valor: "))
    if n.isnumeric():
        int(n)
        leia_int(n)
        resp = str(input(f"Deseja continuar ? ({cores["verde"]}S/{cores["vermelho"]}N):{cores["limpa"]} ")).strip().upper()
        if resp == "N":
            break
    else:
        print(f"{cores["vermelho"]}ERRO! Por favor, digite um número inteiro.")
        continue
print(f"Por hoje é só. Muito obrigado!")
