from math import factorial

def fatorial(n):
    fat = factorial(n)
    print(f"O fatorial do número {n} é {fat}")

# Programa principal
num = int(input("Digite um valor: "))
fatorial(num)
