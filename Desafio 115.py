from time import sleep
from Modulo115a2 import *
from sistema import *

arq =  "cursoemvideo.txt"

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resp = menu(["Ver pessoas cadastradas", "Cadastrar nova Pessoa", "Sair do sistema"])
    if resp == 1:
        # Opção de listar o conteúdo de um arquivo
       lerarquivo(arq)
    elif resp == 2:
        cabecalho("Novo cadastro")
        nome = str(input("Nome: "))
        idade = leiaint("Idade: ")
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabecalho(f"Saindo do sistema... Até mais!")
        break
    else:
        print("\033[31mERRO: digite uma opção válida.\033[m")
    sleep(1)
