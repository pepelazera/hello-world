from Modulo01 import *
from arquivoTXT import *

arq = "arquivoteste.txt"
if not arquivoexiste(arq):
        criarquivo(arq)
else:
        print(f"Arquivo {arq} encontrado com sucesso!")

while True:
        menu("Banco de dados")
        options("[1] Cadastrar uma pessoa\n"
                "[2] Ver cadastros salvos em .txt\n"
                "[3] Ver os cadastros salvos em .json\n"
                "[4] Sair do programa")
        linha()
        try:
                resp = int(input("Sua opção: "))
                if resp == 1:
                        menu("Cadastrar uma nova pessoa")
                elif resp == 2:
                        menu("Ver cadastros salvos em .txt")
                elif resp == 3:
                        menu("Ver cadastros salvos em .json")
                elif resp == 4:
                        print("Saindo do programa...")
                        break
                elif resp > 4:
                        print("ERRO: por favor, digite uma opção válida.")
        except (ValueError, TypeError):
                print("ERRO: por favor, digite um número que seja válido.")
        except KeyboardInterrupt:
                print("O usuário não escolheu nenhuma opção.")
                break