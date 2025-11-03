from sistemaT2 import *
while True:
    try:
        print("\n--- Sistema de Reservas ---")
        print("1. Fazer reserva")
        print("2. Cadastrar novo voo")
        print("3. Listar voos")
        print("4. Cancelar reserva")
        print("5. Encerrar sistema")

    except (ValueError, TypeError):
        print("ERRO: Opcao Invalida.")


    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            print("\n--- Fazer Reserva ---")
            nome = input("Nome do passageiro: ")
            num = input("Número do voo: ")
            classe = input("Classe (Economica, Executiva e Primeira Classe): ").strip().upper()

            print()
            fazer_reserva(nome, num, classe)

        case 2:
            print("\n--- Cadastrar Novo Voo ---")
            num = input("Número do novo voo: ")
            dest = input("Destino do voo: ")

            resultado = cadastrar_voo(num, dest)
            print(resultado)

        case 3:
            print("\n--- Voos Disponíveis ---")
            print(listar_voos())

        case 4:
            print("\n--- Cancelar Reserva ---")
            codigo = input("Digite o código da reserva para cancelar: ")
            resultado = cancelar_reserva(codigo)
            print(resultado)

        case 5:
            print("Saindo do sistema...")
            break

        case _:
            print("Opção inválida. Tente novamente.")
