from time import sleep
viagem = float(input('Qual a distancia da sua viagem em Km ? '))
valor1 = (viagem * 0.5) 
valor2 = (viagem * 0.45)

if viagem < 200:
    print(f'O preco da sua viagem foi de R${valor1}') 
elif viagem > 200:
    print(f'O preco da sua viagem foi de R${valor2}')