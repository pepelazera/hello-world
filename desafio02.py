def leia_vogal(f):
    c_vogal = 0
    for letra in f:
        if letra in "aeiou":
            c_vogal += 1
    print(f"Existem {c_vogal} vogais na frase.")


# Programa principal
frase = str(input("Digite uma frase: ").strip().lower())
leia_vogal(frase)
