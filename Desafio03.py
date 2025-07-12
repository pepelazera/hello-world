# Importações
from time import sleep

while True:
    try:
        v1 = float(input("Digite o primeiro valor: "))
        v2 = float(input("Digite o segundo valor: "))
        o = str(input("Digite um operador: "))
        if o == "+":
            r = v1 + v2
            print(r)
        elif o == "-":
            r = v1 - v2
            print(r)
        elif o == "*":
            r = v1 * v2
            print(r)
        elif o == "/":
            r = v1 / v2
            print(r)
        else:
            print("ERRO: Por favor, digite uma opção válida")
        c = str(input("Deseja continuar ? (S/N): ")).strip().upper()
        if c == "S":
            continue
        elif c == "N":
            print("Encerrando calculadora...")
            sleep(1.5)
            print("")
            print("Programa encerrado. Obrigado pelo uso!")
            break
        else:
            print("Pare de gracinhas.")
    except (ValueError, TypeError):
        print("ERRO: Por favor, digite uma opção válida")
        continue
    except ZeroDivisionError:
        print("ERRO: Não é possível fazer uma divisão por zero")
        continue
    except KeyboardInterrupt:
        print("Usuário encerrou o programa")
        break