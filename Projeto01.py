from Modulo01 import *
from arquivoTXT import *

arq = "arquivoteste.txt"
if not arquivoexiste(arq):
        criarquivo(arq)
else:
        print(f"Arquivo {arq} encontrado com sucesso!")

while True:
        menu("\033[35mBanco de dados\033[m")
        options("\033[32m[1] \033[35mCadastrar uma pessoa\033[m\n"
                "\033[32m[2] \033[35mVer cadastros salvos em .txt\033[m\n"
                "\033[32m[3] \033[35mVer os cadastros salvos em .json\033[m\n"
                "\033[32m[4] \033[35mSair do programa\033[m")
        linha()
        try:
                resp = int(input("\033[32mSua opção: \033[m"))
                if resp == 1:
                        menu("\033[35mCadastrar uma nova pessoa\033[m")
                        nome = str(input("\033[32mNome: \033[m"))
                        idade = leiaint("\033[32mIdade: \033[m")
                        cadastrarpessoa(arq, nome, idade)
                elif resp == 2:
                        menu("\033[35mVer cadastros salvos em .txt\033[m")
                        lerarquivo(arq)
                elif resp == 3:
                        menu("\033[35mVer cadastros salvos em .json\033[m")
                elif resp == 4:
                        print("\033[33mSaindo do programa...\033[m")
                        break
                elif resp > 4:
                        print("\033[31mERRO: por favor, digite uma opção válida.\033[m")
        except (ValueError, TypeError):
                print("\033[31mERRO: por favor, digite um número que seja válido.\033[m")
        except KeyboardInterrupt:
                print("\033[33mO usuário não escolheu nenhuma opção.\033[m")
                break
