def menu(msg):
    print("-"*55)
    print(msg)
    print("-"*55)


def options(msg):
    print(msg)

def linha():
    print("-"*55)

def resp(txt):
    while True:
        try:
            r = int(input(txt))
            if r == 3:
                print("-"*55)
                print("Saindo do sistema... Até mais!".center(55))
                print("-"*55)
                break
            while True:
                if r > 3:
                    print(f"\033[31mERRO: Digite uma opção válida.\033[m")
                    break
                else:
                    print("-"*55)
                    print(f"Opção {r}".center(55))
                    print("-"*55)
                    break
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número válido.\033[m")
        except KeyboardInterrupt:
            print("\033[34mO usuário preferiu não informar os dados.\033[m")
            break
