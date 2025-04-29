def area(larg, comp):
    A = larg * comp
    print(f'A área de um terreno {larg}x{comp} é {A:.2f}m².')

# Programa principal
print('Controle de terrenos')
print('-'*20)
l = float(input('LAGURA: '))
c = float(input('COMPRIMENTO: '))
area(l, c)