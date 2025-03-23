from time import sleep
soma = 0

while True:
    entrada = input("Digite um valor (999 para parar): ")

    try:
        num = int(entrada)

        if num == 999: 
            sleep(0.5)
            print('')
            print("Encerrando programa")
            break
     
        soma += num

    except ValueError:
       print("Caractéres inválidos. Digite um valor válido.")
       print('')

sleep(1.2)
print('')
print(f"A soma de todos os valores digitados é {soma}.")