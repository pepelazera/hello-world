from time import sleep
from Modulo115 import *
from sistema import *

arq = "cursoemvideo.txt"

if not arquivoextiste(arq):
    criararquivo(arq)


while True:
    resp = menu(["Ver pessoas cadastradas", "Cadastrar nova Pessoa", "Sair do sistema"])
    if resp == 1:
        lerarquivo(arq)
    elif resp == 2:
        cabecalho("Opção 2")
    elif resp == 3:
        cabecalho(f"Saindo do sistema... Até mais!")
        break
    else:
        print("\033[31mERRO: digite uma opção válida.\033[m")
    sleep(1)