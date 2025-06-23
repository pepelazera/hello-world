with open ("livros.txt", "r", encoding="utf-8") as arquivo:
    i = 0
    for linha in arquivo:
        i += 1
        print(f"{i} - {linha.rstrip()}")