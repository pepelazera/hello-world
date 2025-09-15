# Controle de Estoque de Livros - versão rústica (2 cadastros fixos)

# níveis mínimos
min_romance = 15
min_ficcao = 10
min_classico = 12

total = 0
romance = 0
ficcao = 0
classico = 0

print("=== CADASTRO DE LIVROS ===")

# livro 1
while True:
    titulo1 = input("Título do livro 1: ")
    genero1 = input("Gênero: ")
    qtd1 = int(input("Quantidade: "))
    total += qtd1
    if genero1.lower() == "romance":
        romance += qtd1
        break
    elif genero1.lower() == "ficção" or genero1.lower() == "ficcao":
        ficcao += qtd1
        break
    elif genero1.lower() == "clássico" or genero1.lower() == "classico":
        classico += qtd1
        break
    else:
        print("ERRO: Não temos essa categoria disponível.")

# livro 2
while True:
    titulo2 = input("\nTítulo do livro 2: ")
    genero2 = input("Gênero: ")
    qtd2 = int(input("Quantidade: "))
    total += qtd2
    if genero2.lower() == "romance":
        romance += qtd2
        break
    elif genero2.lower() == "ficção" or genero2.lower() == "ficcao":
        ficcao += qtd2
        break
    elif genero2.lower() == "clássico" or genero2.lower() == "classico":
        classico += qtd2
        break
    else:
        print("ERRO: Não temos essa categoria disponível.")

# relatório
print("\n=== RELATÓRIO DE ESTOQUE ===")
print("Total de livros:", total)

if total > 0:
    print("\nPercentual de cada título:")
    print(f"- {titulo1} ({genero1}): {(qtd1/total)*100:.2f}%")
    print(f"- {titulo2} ({genero2}): {(qtd2/total)*100:.2f}%")

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
