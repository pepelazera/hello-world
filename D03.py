def linha():
    print("-"*40)

def criararquivo():
    r = input("Escreva um nome: ")
    if r:
        with open("nomes.txt", "a") as arquivo:
            arquivo.write("\n" + r)
        print("\nNome cadastrado com sucesso.")
    else:
        print("\nNome vazio. Nada foi salvo.")

def leraquivo():
    with open("nomes.txt", "r") as arquivo:
        linhas = arquivo.readlines()

        nomes = []
        for linha in linhas:
            nome = linha.strip()
            if nome != "":
                nomes.append(nome)

        nomes_ordenados = sorted(nomes)

        if nomes_ordenados:
            print("Lista de nomes: ")
            for nome in nomes_ordenados:
                print(f"- {nome}")


# Programa principal
while True:
    try:
        linha()
        print("[1] Cadastrar novo nome\n"
              "[2] Listar nomes cadastrados\n"
              "[3] Sair")
        linha()
        print("")

        resp = int(input("Escolha uma opção: "))
        if resp == 1:
            linha()
            print("Cadastrando novo nome...")
            criararquivo()
            linha()
            print("")
            print("         Nome cadastrado com sucesso!")
            print("")
        elif resp == 2:
            linha()
            print("Carregando lista de usuários...")
            linha()
            print("")
            print("Lendo arquivo...")
            leraquivo()
            print("")
        elif resp == 3:
            linha()
            print("Encerrando programa...")
            linha()
            break
        else:
            print("ERRO: Por favor, digite uma opção válida.")
    except (ValueError, TypeError):
        print("ERRO: Por favor, digite uma opção válida.")
        continue
    except KeyboardInterrupt:
        print("O usuário encerrou o programa.")
        break