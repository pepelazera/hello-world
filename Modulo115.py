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

def linha(tam=55):
    return "-"*tam

def cabecalho(txt):
    print(linha())
    print(txt.center(55))
    print(linha())

def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
        c += 1
    print(linha())
    opc = leiaint("\033[32mSua opção: \033[m")
    return opc