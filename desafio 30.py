from time import sleep
numero = int(input('Digite um numero qualquer: '))
print('Processando...')
sleep(2)

if numero % 2 == 0: 
    print(f'O mumero eh par: {numero}')
else:
    print(f'O numero eh impar: {numero}')

