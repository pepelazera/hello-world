from ModuloSacana import *

def arquivoexiste(arq):
    try:
        a = open(arq, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(nome):
    try:
        a = open(nome, "wt+") # Cria o arquivo caso ele não exista
        a.close()
    except:
        print("Houve um erro na criação do arquivo.")
    else:
        print(f"Arquivo {nome} criado com sucesso.")

def lerarquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("Erro ao ler o arquivo.")
    else:
        menuprincipal("Pessoas cadastradas")
        for linha2 in a:
            dado = linha2.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close()

def cadastrarpessoa(arq, nome="desconhecido", idade=0):
    try:
        a = open(arq, "at") # Coloca algo dentro do arquivo.
    except:
        print("\033[31mHouve um erro na abertura do arquivo.\033[m")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("\033[31mHouve um erro na escrita dos dados.\033[m")
        else:
            print(f"Novo registro de {nome} adicionado.")
            a.close()