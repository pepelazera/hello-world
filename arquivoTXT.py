def arquivoexiste(arq):
    try:
        arquivo = open(arq, "r")
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
        print("ERRO: ocorreu algum problema na criação do arquivo.")
    else:
        print(f"Arquivo {arq} criado.")
