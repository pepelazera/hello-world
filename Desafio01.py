def fatorial(n):
    r = 1
    for f in range(n, 0, -1):
        r = r * f
    print(f"O fatorial de {n} é {r}")
    return r


# Programa principal
num = int(input("Digite um número: "))
fatorial(num)
