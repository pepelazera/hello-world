from time import sleep

while True:
    num1 = int(input('Digite um valor: '))
    num2 = int(input('Digite outro valor: '))
    soma = num1 + num2
    muliplicar = num1 * num2
    maiornum = 0

    print('     [ 1 ] somar     ')
    print('     [ 2 ] multiplicar       ')
    print('     [ 3 ] maior     ')
    print('     [ 4 ] novos números     ')
    print('     [ 5 ] sair do programa      ')
    print('')
    escolha = int(input("Qual a sua opção ? "))
    print('')
    print("Processando...")
    print('')
    sleep(1.2)
        
    while escolha not in (1, 2, 3, 4, 5):
            escolha = int(input("Inválido. Selecione caractéres válidos: "))
            print('')
        
    if escolha == (1):
        print("A soma entre {} e {} é {}".format(num1, num2, soma))
        print('')

    if escolha == (2):
        print("A multiplicação entre {} e {} é {}".format(num1, num2, muliplicar))
        print('')

    if escolha == (3):
        if num1 > num2:
            print("Você escolhou os números {} e {}. O maior entre eles é {}".format(num1, num2, num1))
            print('')
        elif num2 > num1:
            print("Você escolheu os números {} e {}. O maior entre eles é {}".format(num2, num1, num2))
            print('')
        else:
            print("Os números são iguais.")
            print('')

    if escolha == (4):
        continue

    if escolha == (5):
        print("Por hoje é só. Muito obrigado!")
        break