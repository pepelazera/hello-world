from ModuloSacana import *
from Sisteminha import *
from time import sleep

arq = "cursoemvideo.txt"
if not arquivoexiste(arq):
    criararquivo(arq)
else:
    print(f"Arquivo {arq} encontrado!")

while True:
    try:
        menuprincipal("Menu Principal")
        opc()
        resp = int(input("\033[32mSua opção: \033[m"))
        if resp == 1:
            lerarquivo(arq)
        elif resp == 2:
            menuprincipal("Cadastrando nova pessoa")
            nome = str(input("Nome: "))
            idade = leiaint("Idade: ")
            cadastrarpessoa(arq, nome, idade)
        elif resp == 3:
            print("Saindo do sistema... Até mais.")
            break
        elif resp > 3:
            print("\033[31mERRO: por favor, digite um número válido.\033[m")
    except (ValueError, TypeError):
        print("\033[31mERRO: por favor, digite um número válido.\033[m")
    except KeyboardInterrupt:
        print("\033[33mO usuário não digitou nenhum valor.\033[m")
    sleep(1)
    
