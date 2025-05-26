from Modulo01 import *

def arquivoexiste(arq):
    try:
        arquivo = open(arq, "r")
        conteudo = arquivo.read()
        print(conteudo)
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarquivo(arq):
    try:
        arquivo = open(arq, "x")
        arquivo.close()
    except (ValueError, TypeError):
        print("\033[31mERRO: ocorreu algum problema na criação do arquivo.\033[m")
    else:
        print(f"Arquivo {arq} criado.")

def lerarquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("\033[31mERRO: Não foi possível ler o arquivo.\033[m")
    else:
        menu("\033[32mMenu Principal\033[m")
        for linha2 in a:
            dado = linha2.split(";")
            dado[1] = dado[1].replace("\n","")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close()

def cadastrarpessoa(arq, nome="<desconhecido>", idade=0):
    try:
        a = open(arq, "at")
    except:
        print("\033[31mERRO: não foi possível abrir o arquivo.\033[m")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("033[31mERRO: houve um erro na escrita dos dados.\033[m")
        else:
            print(f"Novo registro de {nome} adicionado.")
            a.close()