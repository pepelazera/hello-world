def metade(n=0, formato=False):
    res = n/2
    return res if formato is False else moeda(res)


def diminuir(n=0, t=0, formato=False):
    res = n - (n * t/100)
    return res if formato is False else moeda(res)


def dobro(n=0, formato=False):
    res = n*2
    return res if formato is False else moeda(res)


def aumentar(n=0, t=0, formato=False):
    res = n + (n * t / 100)
    return res if formato is False else moeda(res)


def moeda(n=0, moeda="R$"):
    return f"{moeda}{n:>.2f}".replace(",", ".")

def resumo(valor=0, taxaa=10, taxar=5):
    print("-"*30)
    print("Resumo do valor".center(30))
    print("-"*30)
    print(f"Preço analisado: \t{moeda(valor)}") # O \t é uma tabulação que serve para alinhar e ajustar o código da maneira correta.
    print(f"Dobro do preço: \t{dobro(valor, True)}")
    print(f"Metade do preço: \t{metade(valor, True)}")
    print(f"{taxaa}% de aumento: \t{aumentar(valor, taxaa, True)}")
    print(f"{taxar}% de redução: \t\t{diminuir(valor, taxar, True)}")
    print("-"*30)