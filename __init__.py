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


def moeda(n=0, m="R$"):
    return f"{m}{n:.2f}"


def resumo(valor=0, taxaa=0, taxar=0):
    print("-"*30)
    print("Resumo do valor".center(30))
    print("-"*30)
    print(f"Preço analisado: \t{moeda(valor)}")
    print(f"Dobro do preço: \t{dobro(valor, True)}")
    print(f"Metade do preço: \t{metade(valor, True)}")
    print(f"{str(taxaa).rjust(4)}% de aumento: \t{aumentar(valor, taxaa, True)}")
    print(f"{str(taxar).rjust(4)}% de redução: \t{diminuir(valor, taxar, True)}")
    print("-"*30)
