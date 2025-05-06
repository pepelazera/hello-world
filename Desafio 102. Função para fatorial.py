def fatorial(n, show=False):
    """
        -> Calcula o Fatorial de um número;
         - para n: O número a ser calculado;
         - para show: (opcional) Mostrar ou não a conta;
         - return: O valor o fatorial de um número n.
        """

    f = 1
    for c in range(n, 0, -1):
        f *= c
    if show is False:
        print(f'{f}')
    elif show is True:
        print(f'{n}', end='')
        for c in range(n-1):
            print(f' x {n-c-1}' , end='')
        print(f' = {f}')
    return f


# Programa principal
fatorial(6, True)
help(fatorial)