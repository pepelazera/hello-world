from moduloprojeto02 import *


arquivo = "Sistemaclientes.txt"

while True:
    try: 
        while True:
            linha()
            menuprincipal()
            linha()
            resp = int(input("Sua opção: "))
            if resp > 5:
                print("ERRO: por favor, digite uma opção válida.")
                continue
            elif resp == 1:
                menu("Cadastrando pessoa")
                nome = str(input("Nome: "))
                idade = leiaint("Idade: ")
            elif resp == 2:
                menu("Cadastrando endereço de cliente")
            elif resp == 3:
                menu("Consultando cliente")
            elif resp == 4:
                menu("Consultando banco de dados")
            elif resp == 5:
                print("Encerrando programa...")
                break
        break
    except (ValueError, TypeError):
        print("ERRO: por favor, digite uma opção válida.")
    except KeyboardInterrupt:
        print("O usuário não digitou nenhuma opção.")
        break