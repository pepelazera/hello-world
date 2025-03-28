numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

def maior(n1, n2):
    if n1 > n2:
        return n1 
    elif n2 > n1:
        return n2
    else:
        return n1 == n2
    
resultado = maior(numero1, numero2)

print(f"O maior valor digitado foi {resultado}.")