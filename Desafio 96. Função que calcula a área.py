print('Controle de terrenos.')
print('-'*20)
print('')

def area():
    largura = float(input('Largura: '))
    comprimento = float(input('Comprimento: '))
    A = largura * comprimento
    print(f'A área de um terreno de {largura}x{comprimento} é de {A:.2f}m2')


area()

