cont = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 
    'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte']

while True:
    numero0a20 = int(input('Digite um número entre 0 a 20: '))

    if numero0a20 < 0 or numero0a20 > 20:
        print('Por favor, digite números válidos.')
        print('')
        continue
    else:
        print('')
        print(f'Você digitou o número {cont[numero0a20]}.')
        break