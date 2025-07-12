# Importações
from time import sleep

while True:
    try:
        def calculadora(x,y, o):
            if o == "+":
                r = x + y
                return r
            elif o == "-":
                r = x - y
                return r
            elif o == "*":
                r = x * y
                return r
            elif o == "/":
                r = x / y
                return r
            return "ERRO: Por favor, digite uma opção válida"
        print("")


        # Programa principal
        xvalor = float(input("Digite o primeiro valor: "))
        yvalor = float(input("Digite o segundo valor: "))
        operador = str(input("Qual operador deseja utilizar ? "))
        resultado = calculadora(xvalor, yvalor, operador)
        print(f"Resultado: {resultado}")
        r2 = str(input("Deseja continuar ? (S/N): ")).strip().upper()
        if r2 == "S":
            print("")
            continue
        elif r2 == "N":
            print("Encerrando a calculadora...")
            sleep(1.5)
            print("Obrigado por utilizar o programa!")
            break

    # Tratamento de erros
    except (ValueError, TypeError):
        print("ERRO: Por favor, tente novamente ")
    except ZeroDivisionError:
        print("ERRO: Não é possível fazer uma divisão por zero")
    except KeyboardInterrupt:
        print("Usuário encerrou o programa")
