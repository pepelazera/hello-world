from time import sleep

def contador(i, f, p):
    print('-'*40)
    print(f'Contagem de {i} até {f} de {p} em {p}.')

    if p < 0:
        p *= -1
    elif p == 0:
        p = 1

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end='  ')
            sleep(0.3)
            cont += p
        print('Fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end='  ')
            sleep(0.3)
            cont -= p
        print('FIM')
    print('-'*40)
    print('')


# Programa principal
contador(1, 10, 2)
contador(10, 0, 2)
print('-'*40)
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
