from time import sleep
def contador(i, f, p):
    print('~'*40)
    print(f'Contagem de {i} a {f} de {p} em {p}.')

    if p == -1:
        p *= -1
    elif p == 0:
        p = 0

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}  ', end='')
            sleep(0.3)
            cont -= p
        print('FIM!')
    print('~'*40)
    print('')


# Programa principal
contador(1, 10, 1)
contador(10, 1, 2)
print('~'*40)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
