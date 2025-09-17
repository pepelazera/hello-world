# Variáveis

minRomance = 15
minFiccao = 12
minSuspense = 14
minClassico = 11

# Estrutura livro
total = 0
romance = 0
ficcao = 0
suspense = 0
classico = 0

livros = []

print("=== Registro de entrada de livros ===")

while True:
    resp = int(input("Escreva o números de registros que deseja fazer: "))
    if resp <= 0:
        print(f"ERRO: Não é possível cadastrar {resp} livros.")
    else:
        print(f"Quantidade de livros que serão cadastrados: {resp}")
        for i in range(resp):
            print(f"\nCadastro do livro {i+1}")
            titulo = input("Título: ")
            genero = input("Gênero: ")
            qtd = int(input("Quantidade: "))

            total += qtd
            if genero.lower() in ["romance"]:
                romance += qtd
            elif genero.lower() in ["ficção", "ficcao"]:
                ficcao += qtd
            elif genero.lower() in ["suspense"]:
                suspense += qtd
            elif genero.lower() in ["classico", "clássico"]:
                classico += qtd
            else:
                print("ERRO: Não temos essa categoria disponível. Livro não contabilizado.")
                continue

            livros.append({"titulo": titulo, "genero": genero, "quantidade": qtd})
    break

print("\n=== Relatório de estoque ===")
print(f"Total de livros: {total}")

# relatório
print("\n=== RELATÓRIO DE ESTOQUE ===")
print("Total de livros:", total)

if total > 0:
    print("\nPercentual de cada título:")
    for livro in livros:
        print(f"- {livro['titulo']} ({livro['genero']}): {(livro["quantidade"] / total) * 100:.2f}%")

print("\n=== VERIFICAÇÃO DE NÍVEIS MÍNIMOS ===")
if romance < minRomance:
    print(f"Romance está abaixo do mínimo: ({romance} / {minRomance})")
else:
    print(f"Romance está dentro dos parâmetros: ({romance})")

if suspense < minSuspense:
    print(f"Romance está abaixo do mínimo: ({suspense} / {minSuspense})")
else:
    print(f"Romance está dentro dos parâmetros: ({suspense})")

if ficcao < minFiccao:
    print(f"Ficção está abaixo do mínimo: ({ficcao} / {minFiccao})")
else:
    print(f"Ficção está dentro dos parâmetros: ({ficcao})")

if classico < minClassico:
    print(f"Clássico está abaixo do mínimo: ({classico} / {minClassico})")
else:
    print(f"Clássico está dentro dos parâmetros: ({classico})")
