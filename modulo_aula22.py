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


def moeda(valor=0, aum=0, dim=0, t=0):
    aum = valor + (valor * aumentar(aum) / 100)
    dim = valor - (valor * diminuir(dim) / 100)
    moeda2 = "R$"
    print("-" * 30)
    print("       Resumo do valor")
    print("-" * 30)
    print(f"Preço analisado:    {moeda2}{valor:.2f}".replace(".",","))
    print(f"Dobro do preço:     {moeda2}{dobro(valor):.2f}".replace(".",","))
    print(f"Metade do preço:    {moeda2}{metade(valor):.2f}".replace(".",","))
    print(f"20% de aumento:     {moeda2}{aum:.2f}".replace(".","."))
    print(f"12% de redução:     {moeda2}{dim:.2f}".replace(".",","))
    print(f"-"*30)
    return f"{moeda2}{valor:.2f}".replace(".", ",")
