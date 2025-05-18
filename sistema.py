from Modulo115 import *
def arquivoextiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(msg):
    try:
        a = open(msg, "wt+") # Escreve um arquivo de texto, e caso não exista, ele cria um
        a.close()
    except:
        print("Houve um erro na criação do arquivo.")
    else:
        print(f"Arquivo {msg} criado com sucesso!")


def lerarquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("Erro ao ler o arquivo.")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        print(a.read())