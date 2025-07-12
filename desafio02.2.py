def leia_vogal(f):
    c = 0
    for letra in f:
        if letra in "aeiou":
            c += 1
    print(f'Na frase "{f}" existem {c} vogais.')


# Programa principal
frase =  str(input("Digite uma frase: "))
leia_vogal(frase)