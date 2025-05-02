from time import sleep
def parametros(* num):
    quant = len(num)
    if quant == 0: # Identificando o valor 0
        print('-'*50)
        print('Foram informados 0 valores ao todo.')
        print('O maior valor informado foi 0')
        sleep(0.5)
    else: # Separando os números normais do 0
        print('-'*50)
        print(f"{' '.join(map(str, num))} Foram informados {quant} valores ao todo.")
        print(f"O maior valor informado foi {max(num)}.")
        sleep(0.5)


# Programa principal
parametros(2, 9, 5, 7, 1)
parametros(4, 7, 0)
parametros(1, 2)
parametros(6)
parametros()
