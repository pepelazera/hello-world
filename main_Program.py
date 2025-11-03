from sistemaT2 import *


while True:
    print("\n--- Sistema de Reservas ---")
    print("1. Fazer reserva")
    print("2. Cadastrar novo voo")
    print("3. Listar voos")
    print("4. Sair")


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

            resultado = cadastrar_voo(nome, num, dest)
            print(resultado)

        case 3:
            print("\n--- Voos Disponíveis ---")
            print(listar_voos())

        case 4:
            print("Saindo do sistema...")
            break

        case _:
            print("Opção inválida. Tente novamente.")