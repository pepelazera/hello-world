from idlelib.replace import replace


def metade(n=0):
    met = n/2
    return met


def dobro(n=0):
    d = n*2
    return d


def aumento10(n=0):
    a = n+(n*0.1)
    return a

def moeda(n=0, m = "R$"):
    return f"{m}{n:.2f}".replace(".", ",")