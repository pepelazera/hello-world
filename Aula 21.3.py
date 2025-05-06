def funcao():
    """
    -> Esse código serve de maneira muito boa para explicar o escopo global e local;
    - No caso, deixei escrito nos prints onde está cada um para que fique mais fácil de compreender;
    - Mesmo com 2 N1 no código, eles tem valores diferentes, pois um é um escopo global e o outro local.
    """
    n1 = 4
    print(f'N1 local vale {4}')

n1 = 2
funcao()
print(f'N1 global vale {n1}')
help(funcao)