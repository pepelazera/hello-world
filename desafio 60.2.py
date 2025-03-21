while True:
    n = int(input("Digite um número para calcular seu fatorial: "))
    c = n 
    f = 1
    print("Calculando {}! = ".format(n), end="")
    while c > 0:
        print("{:.2f}".format(c), end='')
        print(" x " if c > 1 else " = ", end="")
        f *= c
        c -= 1
    print("{:.2f}".format(f))
    final = str(input("Deseja testar outro número (S/N) ? ")).strip().upper()
    if final == 'S':
        print('Reiniciando...')
    elif final == 'N':
        print('')
        print('Por hoje é só. Muito obrigado!')
        break