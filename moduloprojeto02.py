def linha():
    print("-"*50)
    

def menuprincipal():
    print("[1] Cadastrar pessoa\n"
          "[2] Cadastrar endereço de cliente\n"
          "[3] Consultar cliente\n"
          "[4] Consultar banco de dados\n"
          "[5] Sair")


def menu(msg):
    linha()
    print(msg.center(50))
    linha()


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


def criararquivo(arq):
    try:
        with open(arq, "w") as arquivo:
            arquivo.write()
            print(arquivo)
    except:
        print("Houve um erro na criação do arquivo.")
    else:
        print("Arquivo criado com sucesso!")


def lerarquivo(arq):
    try:
        with open(arq, "r") as arquivo:
            arquivo.read()
    except FileNotFoundError:
        print("Erro ao tentar ler arquivo.")
    else:
        print("Arquivo lido com sucesso.")