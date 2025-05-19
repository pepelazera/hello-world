from time import sleep


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[34mAVISO: usuário preferiu não digitar um valor.\033[m")
            return 0
        else:
            return n


def linha():
    print("-"*55)


def menu(txt):
    linha()
    print(txt.center(55))
    linha()


def opc(txt):
    print(txt)
    linha()


def interface():
    print("\033[33m 1 - \033[34m Ver pessoas cadastradas\033[m")
    print("\033[33m 2 - \033[34m Cadastrar novas pessoas\033[m")
    print("\033[33m 3 - \033[34m Sair do sistema\033[m")
    linha()
