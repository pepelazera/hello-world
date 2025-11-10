fichas = []
arquivo = "fichas.txt"
exercicios_padrao = ("Supino reto", "Supino inclinado com halteres", "crucifixo maquina", "Agachamento no Hack/Smith", "Agachamento livre" ,
                     "Rosca direta", "Rosca scott", "Puxada alta", "Remada baixa no triangulo", "Leg press 45", "Triceps frances na polia", "triceps carter")

def carregar_fichas():
    try:
        with open(arquivo, "r") as f:
            for linha in f:
                dados = linha.strip().split(";")
                # A linha abaixo é a correção:
                ficha = {
                    "nome": dados[0],
                    "objetivo": dados[1],
                    "exercicios": dados[2].split(","),
                    "data": dados[3]
                }
                fichas.append(ficha)
    except FileNotFoundError:
        pass

def salvar_fichas():
    with open(arquivo, "w") as f:
        for ficha in fichas:
            linha = f"{ficha['nome']};{ficha['objetivo']};{','.join(ficha['exercicios'])};{ficha['data']}\n"
            f.write(linha)

carregar_fichas()

while True:
    print("\n===== SISTEMA DE FICHAS DE TREINO =====")
    print("[1] Cadastrar nova ficha")
    print("[2] Consultar ficha por nome")
    print("[3] Listar todas as fichas")
    print("[4] Apagar todos os dados")
    print("[5] Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        ficha = {}
        ficha["nome"] = input("Nome do aluno: ")
        ficha["objetivo"] = input("Objetivo do treino (ex: hipertrofia, emagrecimento): ")

        print("\nSugestões de exercícios padrão:")
        for e in exercicios_padrao:
            print("-", e)

        ficha["exercicios"] = []
        print("\nDigite os exercícios desejados (digite 'fim' para encerrar):")
        while True:
            ex = input("Exercício: ")
            if ex.lower() == "fim":
                break
            ficha["exercicios"].append(ex)

        ficha["data"] = input("Data de início do treino (ex: 09/11/2025): ")
        fichas.append(ficha)
        salvar_fichas()
        print("Ficha cadastrada com sucesso!")

    elif opcao == "2":
        nome_busca = input("Digite o nome do aluno: ")
        encontrado = False
        for ficha in fichas:
            if ficha["nome"].lower() == nome_busca.lower():
                print("\n--- Ficha Encontrada ---")
                print("Nome:", ficha["nome"])
                print("Objetivo:", ficha["objetivo"])
                print("Exercícios:", ", ".join(ficha["exercicios"]))
                print("Data de início:", ficha["data"])
                encontrado = True
                break
        if not encontrado:
            print("Aluno não encontrado.")

    elif opcao == "3":
        if len(fichas) == 0:
            print("Nenhuma ficha cadastrada.")
        else:
            print("\n--- Fichas Cadastradas ---")
            for ficha in fichas:
                print(f"Aluno: {ficha['nome']} | Objetivo: {ficha['objetivo']} | Data: {ficha['data']}")

    elif opcao == "4":
        confirmar = input("Tem certeza que deseja apagar TODOS os dados? (s/n): ")
        if confirmar.lower() == "s":
            fichas = []
            with open(arquivo, "w") as f:
                f.write("")
            print("Todos os dados foram apagados com sucesso!")
        else:
            print("Operação cancelada.")

    elif opcao == "5":
        print("Saindo do programa... Dados salvos.")
        salvar_fichas()
        break

    else:
        print("Opção inválida. Tente novamente.")