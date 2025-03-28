numero1 = int(input("Digite um número: "))

def parimpar(n1):
    parimpar = n1 % 2 == 0
    neutro = n1 == 0
    return n1 


resultado = parimpar(numero1)

if resultado == 0:
    print(f"O número {resultado} é neutro.")
elif resultado % 2 == 0:
    print(f"O número {resultado} é par.")
else:
    print(f"O número {resultado} é ímpar.")