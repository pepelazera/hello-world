# Variáveis
infoConta = {'nome': '', 'numero': 0, 'tipo': ''}

# Programa principal
while True:
    try:
        infoConta['nome'] = input("Digite um nome: ")
        infoConta['numero'] = int(input("Número de conta: "))
        saldoConta = 0
        statusConta = False
        print()

        while True:
            print("[0] Status da Conta\n"
                  "[1] Abrir Conta\n"
                  "[2] Fechar Conta\n"
                  "[3] Sacar\n"
                  "[4] Depositar\n"
                  "[5] Encerrar Atendimento\n")
            opc = int(input("Escolha uma das opções acima: "))
            print()


        # Comandos
            if opc == 1:
                if statusConta is True:
                    print("Conta já existente.")
                else:
                    infoConta['tipo'] = input("Tipo de conta (CC ou CPP): ").strip().lower()

                    if infoConta['tipo'] == "cc":
                        saldoConta = 100
                    elif infoConta['tipo'] == "cpp":
                        saldoConta = 150
                    else:
                        print("ERRO: opção inválida.")
                        continue
                    statusConta = True
                    print("Conta criada com sucesso!")


            elif opc == 0:
                print("=== STATUS DA CONTA ===")
                print(f"Nome de usuário: {infoConta['nome']}\n"
                      f"Número da conta: {infoConta['numero']}\n"
                      f"Tipo da conta: {infoConta['tipo']}")
                print(f"Saldo: R${saldoConta:.2f}")
                print(f"Status: {statusConta}")
                print("=" * 25)
                print()


            elif opc == 2:
                if statusConta is False:
                    print("Erro ao realizar fechamento de conta: Conta não existente.")
                elif saldoConta > 0:
                    print("Erro ao realizar fechamento de conta: Conta com dinheiro.")
                elif saldoConta < 0:
                    print("Erro ao realizar fechamento de conta: Saldo devedor.")
                else:
                    print("Conta fechada com sucesso!\n")
                    statusConta = False

                    print("Encerrando programa...\n")
                    print("=== STATUS DA CONTA ATUAL ===")
                    print(f"Nome de usuário: {infoConta['nome']}\n"
                          f"Número da conta: {infoConta['numero']}\n"
                          f"Tipo da conta: {infoConta['tipo']}")
                    print(f"Saldo: R${saldoConta:.2f}")
                    print(f"Status: {statusConta}")
                    print("=" * 25)
                    print()
                    break


            elif opc == 3:
                if saldoConta < 1:
                    print("ERRO: Você não tem valor suficiente para realizar esse saque.")
                else:
                    saque = float(input("Quanto você irá sacar: "))
                    if saldoConta < saque:
                        print("ERRO: Você não tem valor suficiente para realizar esse saque.")
                    else:
                        print(f"Saque de R${saque:.2f} realizado com sucesso!")
                        saldoConta -= saque


            elif opc == 4:
                if statusConta is False:
                    print("ERRO: Conta não existente.")
                else:
                    deposito = float(input("Quanto deseja depositar ? "))
                    saldoConta += deposito
                    print(f"valor de R${deposito:.2f} depositado com sucesso!")


            elif opc > 5:
                print("ERRO: Por favor, digite uma opção válida.")
                continue


            elif opc == 5:
                print("Encerrando programa...\n")
                print("=== STATUS DA CONTA ATUAL ===")
                print(f"Nome de usuário: {infoConta['nome']}\n"
                      f"Número da conta: {infoConta['numero']}\n"
                      f"Tipo da conta: {infoConta['tipo']}")
                print(f"Sado: R${saldoConta:.2f}")
                print(f"Status: {statusConta}")
                print("=" * 25)
                print()
                break
        break


    except (ValueError, TypeError):
        print("ERRO")
        continue
    except KeyboardInterrupt:
        print("\nPrograma encerrado.")
        break
