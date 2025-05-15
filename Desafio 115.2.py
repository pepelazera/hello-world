from time import sleep

from Modulo115a2 import *

while True:
    resp = menu(["Ver pessoas cadastradas", "Cadastrar nova Pessoa", "Sair do sistema"])
    if resp == 1 or resp == 2:
        cabecalho(f"Opção {resp}")
    elif resp == 3:
        cabecalho(f"Saindo do sistema... Até mais!")
        break
    else:
        print("\033[31mERRO: digite uma opção válida.\033[m")
    sleep(1)