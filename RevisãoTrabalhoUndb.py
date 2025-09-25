# CONFIGURAÇÕES
from django.template.defaultfilters import title
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

min_romance = 15
min_ficcao = 10
min_classico = 12
num_registros = 2

romance = 0
ficcao = 0
classico = 0

titulo = str
genero = str
quantidade = 0

# ARMAZENAMENTO E CÁLCULOS
estoque = []
total_livros = 0
porcentagem: float

# Processo
print("=== REGISTRO DE ENTRADA DE LIVROS ===")

for i in range(num_registros):
    livro = {'titulo': '', 'genero': '', 'quantidade': 0}

    print()
    print(f"Livro {i+1}: ")

    titulo = input("Título: ")
    livro['titulo'] = titulo

    genero = input("Gênero: ")
    livro['genero'] = genero

    quantidade = int(input("Quantidade: "))
    livro['quantidade'] = quantidade

    if livro['genero'].lower() == "romance":
        romance += quantidade
    elif livro['genero'].lower() in ['clássico', 'classico']:
        classico += quantidade
    elif livro['genero'].lower() in ['ficção', 'ficçao', 'ficcão', 'ficcao']:
        ficcao += quantidade

    estoque.append(livro)
    total_livros += livro['quantidade']

# RELATÓRIO
print("=== RELATÓRIO DE ESTOQUE ===")
print(f"Total de livros: {total_livros}")
print()

if total_livros > 0:
    print("Percentual por título/gênero: ")
    print()

    for livro in estoque:
        porcentagem = (livro['quantidade'] / total_livros) * 100

        print(f"- {livro['titulo']} - {livro['genero']}: {porcentagem:.2f}%")
        print(f"- Quantidade: {livro['quantidade']}")
        print()

if romance < min_romance:
    print("Romance está abaixo do mínimo necessário.")
else:
    print("Romance está dentro da quantidade recomendada.")

if ficcao < min_ficcao:
    print("Ficção está abaixo do mínimo necessário.")
else:
    print("Ficção está dentro da quantidade recomendada.")

if classico < min_classico:
    print("Clássico está abaixo do mínimo necessário.")
else:
    print("Clássico está dentro da quantidade recomendada.")