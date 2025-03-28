numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

def media(n1, n2):
    media = (n1 + n2) / 2 
    return media

resultado = media(numero1, numero2)

print(f"A média é {resultado}.")