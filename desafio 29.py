x = float(input('Qual a velocidade atual do carro ? '))

if x > 80: 
    ab = False
    print('MULTADO! Voce excedeu o limite de velocidade permitido que eh de 80km/h')
    print('Voce pagara uma multa de', ((x - 80)*7))

else: 
    print('Tudo certo. Voce esta dentro do limite de velocidade permitido pela via')