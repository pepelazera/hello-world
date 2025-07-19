def registrar_nome(n):
    with open("nomes.txt", "a") as arquivo:
        arquivo.write(f"{n}\n")


# Programa principal
while True:
    nome = input("Digite um nome: ")
    registrar_nome(nome)
    print(f"O nome foi salvo em um arquivo")
    try:
        r = input("Deseja cadastrar outro nome ? (S/N): ").lower().strip()
        if r == "s":
            continue
        elif r == "n":
            print("Por hoje é só!")
            break
        else:
            print("ERRO: Por favor, digite uma opção válida")
    except (ValueError, TypeError):
        print("ERRO: Por favor, digite uma digite uma opção válida.")
    except KeyboardInterrupt:
        print("O usuário encerrou o programa sem escrever nada.")
        break
