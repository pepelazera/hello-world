from Modulo115 import *
from sistema import *
from time import sleep

arq = "cursoemvideo.txt"

if arquivoexiste(arq):
    print("Arquivo encontrado!")
else:
    print("Arquivo não encontrado.")
    criararquivo(arq)

menu("PESSOAS CADASTRADAS")
interface()

while True:
    try:
        resp = int(input("\033[32mSua opção: \033[m"))
        if resp == 1:
            #Opção de listar o conteúdo de um arquivo.
            lerarquivo(arq)
        elif resp == 2:
            linha()
            print("Opção 2".center(55))
            linha()
        elif resp == 3:
            linha()
            print("Saindo do sistema... Até logo!".center(55))
            linha()
            break
    except (ValueError, TypeError):
        print("\033[31mERRO: por favor, digite uma opção válida.\033[m")
    except KeyboardInterrupt:
        print("\033[33mO usuário não escolheu nenhuma opção.\033[m")
        break
    sleep(1)
