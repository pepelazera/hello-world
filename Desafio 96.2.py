def area(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é {a}m²')

print('Controle de terrenos')
print('-'*30)
lar = float(input('Largura: '))
com = float(input('Comprimento: '))
area(lar, com)