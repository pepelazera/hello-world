# Controle de Estoque de Livros - versão corrigida

# níveis mínimos
min_romance = 15
min_ficcao = 10
min_classico = 12

total = 0
romance = 0
ficcao = 0
classico = 0

# lista para armazenar os livros cadastrados
livros = []

print("=== CADASTRO DE LIVROS ===")

while True:
    resp = int(input("Quantos livros deseja cadastrar? "))
    if resp <= 0:
        print(f"ERRO: Não é possível cadastrar {resp} livros.")
    else:
        print(f"Quantidade de livros que serão cadastrados: {resp}")
        for i in range(resp):
            print(f"\nCadastro do livro {i+1}:")
            titulo = input("Título do livro: ")
            genero = input("Gênero: ")
            qtd = int(input("Quantidade: "))

            total += qtd
            if genero.lower() == "romance":
                romance += qtd
            elif genero.lower() in ["ficção", "ficcao"]:
                ficcao += qtd
            elif genero.lower() in ["clássico", "classico"]:
                classico += qtd
            else:
                print("ERRO: Não temos essa categoria disponível. Livro não contabilizado.")
                continue  # não adiciona este livro se o gênero não for válido

            # salva no cadastro
            livros.append({"titulo": titulo, "genero": genero, "qtd": qtd})
    break  # sai do loop principal depois de cadastrar

# relatório
print("\n=== RELATÓRIO DE ESTOQUE ===")
print("Total de livros:", total)

if total > 0:
    print("\nPercentual de cada título:")
    for livro in livros:
        print(f"- {livro['titulo']} ({livro['genero']}): {(livro['qtd']/total)*100:.2f}%")

print("\n=== VERIFICAÇÃO DE NÍVEIS MÍNIMOS ===")
if romance < min_romance:
    print(f"Romance está abaixo do mínimo ({romance}/{min_romance})")
else:
    print(f"Romance está dentro dos parâmetros ({romance})")

if ficcao < min_ficcao:
    print(f"Ficção está abaixo do mínimo ({ficcao}/{min_ficcao})")
else:
    print(f"Ficção está dentro dos parâmetros ({ficcao})")

if classico < min_classico:
    print(f"Clássico está abaixo do mínimo ({classico}/{min_classico})")
else:
    print(f"Clássico está dentro dos parâmetros ({classico})")
