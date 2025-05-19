from Modulo115 import *

def arquivoexiste(arq):
    try:
        a = open(arq, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(arq):
    try:
        a = open(arq, "wt+")
        a.close()
    except:
        print("Houve um erro na criação do arquivo.")
    else:
        print(f"Arquivo {arq} criado com sucesso!")


def lerarquivo(arq):
    try:
        a = open(arq,"rt")
    except FileNotFoundError:
        print("Erro ao ler arquivo.")
    else:
        menu("PESSOAS CADASTRADAS")
        print(a.read())
    finally:
        a.close()


def cadastraralguem(arq, nome="desconhecido", idade=0):
    try:
        a = open(arq, "at")
        a.close()

    except:
        print("Houve um problema na abertura do arquivo.")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Houve um erro na hora de escrever os dados.")
        else:
            print(f"Novo registro {nome} adicionado.")
            a.close()
