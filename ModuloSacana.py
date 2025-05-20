def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[33mAVISO: usuário preferiu não digitar um valor.\033[m")
            return 0
        else:
            return n


def linha():
    print("-"*55)

def menuprincipal(txt):
    linha()
    print(txt.center(55))
    linha()

def opc():
    print("\033[33m1 - \033[34mVer pessoas cadastradas\033[m")
    print("\033[33m2 - \033[34mCadastrar nova pessoa\033[m")
    print("\033[33m3 - \033[34mSair do sistema\033[m")
    linha()

