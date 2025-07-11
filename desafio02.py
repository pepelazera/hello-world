def leia_vogal(f):
    c_vogal = 1
    for l in enumerate(f):
        if "aeiou" in l:
            c_vogal += l
    print(f"Existem {c_vogal} vogais na frase.")


# Programa principal
frase = str(input("Digite uma frase: ").strip().lower())
leia_vogal(frase)
