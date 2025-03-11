#variaveis necessarias
peso = float(input('Qual seu peso ? (Kg) '))
altura = float(input('Qual sua altura ? (M) '))

#calculo do IMC
IMC = (peso / altura**2)
print(f'O IMC dessa pessoa eh de {IMC:.1f}')

#conjunto de condicoes 
if IMC <= 18.5:
    print('Voce esta ABAIXO do seu peso ideal.')
elif IMC >= 18 and IMC <= 25:
    print('Voce esta no peso ideal.')
elif IMC > 25 and IMC <= 30: 
    print('Voce esta com SOBREPESO.')
elif IMC > 30 and IMC < 40: 
    print('Voce esta em um caso de OBESIDADE!')
else: 
    print('Voce esta em um caso de OBESIDADE MORBIDA!')