
def leiaint(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[33mO usuário não informou nenhum valor.\033[m")
            return 0
        else:
            return n

def linha():
    print("\033[32m-\033[m"*55)


def menu(txt):
    linha()
    print(txt.center(55))
    linha()


def options(txt):
    print(txt)

