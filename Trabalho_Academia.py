import random
from time import sleep
from Funcoes_Academia import carregar_dados, salvar_dados

fichas_treino = list()
alunos_cadastrados = list()
novas_fichas = list()

nome_arquivo = "fichas.txt"

alunos_cadastrados = carregar_dados(nome_arquivo)


try:
    while True:
        print("\nEscolha uma opcao: "
              "\n[1] Aluno novo"
              "\n[2] Aluno ja cadastrado"
              "\n[3] Fichas de treino"
              "\n[4] Sair do programa")

        opc = int(input("Ecolha uma opcao: "))

        match opc:
            case 1:

                nova_ficha_aluno = {'divisao': '',
                                    'dias': 0,
                                    'numero de series semanais': random.randint(6,10),
                                    'nome': '',
                                    'objetivo': '',
                                    'exercicios': []
                                    }

                while True:
                    nome_Aluno = input("Nome do aluno: ")
                    nova_ficha_aluno['nome'] = nome_Aluno

                    dias_Livres = int(input("Quantos dias livres voce tem pra treinar ? "))
                    divisao_valida = True

                    match dias_Livres:
                        case 2:
                            nova_ficha_aluno['divisao'] = 'fullbody'
                            nova_ficha_aluno['dias'] = 2

                            print("\nOBS: Nao recomendamos treinar menos de 3x por semana, mas essa divisao seria mais adequada para isso.")


                        case 3:
                            nova_ficha_aluno['divisao'] = 'fullbody'
                            nova_ficha_aluno['dias'] = 3


                        case 4:
                            nova_ficha_aluno['divisao'] = 'Upper/Lower'
                            nova_ficha_aluno['dias'] = 4


                        case 5:
                            nova_ficha_aluno['divisao'] = 'PPL / Upper, Lower'
                            nova_ficha_aluno['dias'] = 5


                        case 6:
                            nova_ficha_aluno['divisao'] = 'PPL 2x'
                            nova_ficha_aluno['dias'] = 6


                        case 7:
                            print("Treinar 7 vezes na semana ? Te recomendo uma terapia...")

                            divisao_valida = False
                            break


                        case _:
                            print("Error: Por favor, digite uma quantidade de dias da semana para continuar: ")
                            continue


            case 2:
                nome_Aluno = input("Digite seu nome: ")
                encontrado = False

                for ficha in alunos_cadastrados:
                    if ficha['nome'] == nome_Aluno:
                        print("\n--- Informacoes do aluno ---")
                        print(ficha)
                        encontrado = True
                        break

                if not encontrado:
                    print("Aluno nao encontrado na lista de cadastro...")

            case 3:
                print(alunos_cadastrados)

            case 4:
                print("Encerrando programa e salvando dados...")
                salvar_dados(nome_arquivo, alunos_cadastrados)

                sleep(0.7)

                print("Programa encerrado com sucesso. Muito obrigado!")
                break

            case _:
                print("Opcao invalida, tente novamente.")

                divisao_valida = False
                continue

        if not divisao_valida:
            continue

        print("gerando divisao...")
        sleep(1.2)

        objetivo = input("Digite o objetivo (ex: hipertrofia, emagrecimento): ").strip()
        nova_ficha_aluno['objetivo'] = objetivo

        print("\n-- Cadastro de Exercicios (digite 'fim' para parar) --")
        while True:
            exercicio = input("Adicionar exercicio: ").strip()
            if exercicio.lower() == 'fim':
                break
            elif exercicio:
                nova_ficha_aluno['exercicios'].append(exercicio)

        print(f"\nDivisao de treino cadastrada: {nova_ficha_aluno}")
        alunos_cadastrados.append(nova_ficha_aluno)

        break


except (ValueError, TypeError):
    print("ERRO: Por favor, digite algo valido")

except KeyboardInterrupt:
    print("O usuario encerrou o programa.")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
    salvar_dados(nome_arquivo, alunos_cadastrados)
