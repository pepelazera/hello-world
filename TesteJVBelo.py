def construtor():
    while True:
        num1 = float(input("Digite um número: "))
        num2 = float(input("Digite outro número: "))
        if num1 or num2 <= 0:
            print("ERRO: por favor, digite novamente: ")
            continue
        else:
            break
    resp = str(input("Qual operador deseja utilizar: (+, -, /, *): "))
    if resp == "+":
         soma(num1, num2)
    elif resp == "-":
        sub(num1, num2)
    elif resp == "*":
        mult(num1, num2)
    elif resp == "/":
        div(num1, num2)


def soma(n1, n2):
    print(n1 + n2)

def sub(n1, n2):
    print(n1 - n2)

def mult(n1, n2):
    print(n1 * n2)

def div(n1, n2):
    print(n1 / n2)
