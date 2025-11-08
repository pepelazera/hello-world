import json
from Trabalho_Academia import *

def carregar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            lista_carregada = json.load(f)
        print("Dados carregados com sucesso!")
        return lista_carregada


    except FileNotFoundError:
        print("Arquivo nao encontrado. Iniciando uma lista vazia...")
        alunos_cadastrados = []
        sleep(0.5)

        print("Lista vazia criada com sucesso.")
        return []


    except json.JSONDecodeError:
        print("ERRO: Nao foi possivel ler arquivo. Iniciando uma lista vazia...")
        alunos_cadastrados = []
        sleep(0.5)

        print("Lista vazia criada com sucesso.")
        return []


def salvar_dados(nome_arquivo, dados_para_salvar):
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados_para_salvar, f, indent=4)


    except IOError as e:
        print(f"Erro ao salvar dados: {e}")


def registrar_ficha():
    print() 