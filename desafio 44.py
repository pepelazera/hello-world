#inicio
from time import sleep
preco = float(input('Preco das compras: R$'))

#opcoes de pagamento
print('')
print('Formas de pagamento: ')
print('[ 1 ] a vista, dinheiro/cheque: desconto de 10%')
print('[ 2 ] a vista, cartao: desconto de 5%')
print('[ 3 ] 2x no cartao: Padrao ')
print('[ 4 ] 3x no cartao: Juros de 20%')

#comando de pagamento
pagamento = int(input('Qual sera a opcao de pagamento ? '))
print('Processando...')
sleep(1.5)
#escolhendo forma de pagamento
if pagamento == 1 or pagamento ==  2 or pagamento == 3 or pagamento == 4: 
    print('')
    print(f'O metodo que voce escolheu foi: {pagamento}')
elif pagamento > 4:
    print('') 
    print('Escolha uma opcao valida')

print('')
print('Processando...')
sleep(1.5)

#variaveis descontos
desconto1 = preco - (preco * 10) / 100 
desconto2 = preco - (preco * 5) / 100 
juros = preco + (preco * 20) / 100

#calculando descontos
if pagamento == 1:
    print('')
    print(f'Sua compra de R${preco} vau custar R${desconto1}')
elif pagamento == 2:
    print('')
    print(f'Sua compra de R${preco} vai custar R${desconto2}')
elif pagamento == 3:
    print('')
    print(f'Sua compra de R${preco} nao tera desconto nem acrescimo')
elif pagamento == 4: 
    print('')
    print(f'Sua compra de R${preco} saira por R${juros}')