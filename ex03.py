arq = "arquivo03.txt"
listarqu = list()


def criarquivo(txt):
    with open(arq, "a") as arquivo:
        arquivo.write(txt)

#Programa principal
while True:

    try:
        r = str(input("O que você quer comprar e quantos ? (Para sair, escreva Nada): "))
        if r == "nada" or r == "Nada" or r == "NADA ":
            break
        else:
            d = r.replace(",", " ")
            criarquivo(d + "\n")
    except (ValueError, TypeError):
        print("ERRO: por favor, digite o que você quer comprar e quantos")
    except KeyboardInterrupt:
        print("O usuário não digitou nenhuma quantidade")
        break
    else:
        continue
with open(arq, "r") as arquivo:
    for linha in arquivo:
        print(f"Você anotou {linha}", end="")
        listarqu.append(linha)


total = len(listarqu)
valores = [int(item.strip().split()[0])for item in listarqu]
print(f"Você precisa comprar ao todo {total} alimentos.")
print(f"Entre eles, você necessita de {sum(valores)} unidades no total.")