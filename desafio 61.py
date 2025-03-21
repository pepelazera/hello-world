from time import sleep

while True:
    print('==' * 10)
    print('10 termos de uma PA')
    print('==' * 10)

    primeirotermo = int(input('Primeiro termo: '))
    razão = int(input('Razão: '))
    quantidadetermos = 10
    contador = 0

    while contador < 11:
        contador = primeirotermo + (quantidadetermos-1) * razão
        contador += 1
        print("")
        print("Processando...")
        sleep(1.2)
        print("")
        print("O resultado do cálculo da PA é {}".format(contador))

    final = str(input("Deseja continuar (S/N) ? ")).strip().upper()
    
    if final == "S":
        print("")
        print("Reiniciando...")
        sleep(1.2)
        print("")
    elif final == "N":
        print("")
        sleep(1.2)
        print("Por hoje é só. Obrigado por testar o cáculo da PA!")
        break