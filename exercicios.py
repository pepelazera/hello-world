num = int(input("Digite um número: "))

tabuada = 0
for c in range(1, 11):
    tabuada = num * c
    print(f"{num} * {c} = {tabuada}")
print()


palavra = input("Digite uma palavra: ").strip().lower()
cPalavra = 0
for letra in palavra:
    if letra in "aeiou":
        cPalavra += 1
    else:
        continue
print(f"Há {cPalavra} vogais na palavra: {palavra}")