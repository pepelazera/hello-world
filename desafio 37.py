numero = int(input('Digite um numero inteiro: '))
print('[ 1 ] converter para BINARIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
numeroescolhido = int(input('Escolha uma opção (1, 2 ou 3): '))

if numeroescolhido == 1:
    binario = bin(numero)[2:]
    print(f'O numero que voce digitou em binario eh {binario}')
elif numeroescolhido == 2:
    octal = oct(numero)[2:]
    print(f'O numero que voce digitou em octal eh {octal}')
elif numeroescolhido == 3:
    hexadecimal = hex(numero)[2:]
    print(f'O numero que voce digitou em hexadecimal eh {hexadecimal}')
else: 
    print('Opção inválida! Escolha 1, 2 ou 3.')