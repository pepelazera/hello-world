valores = []

while True:
    numero = int(input('Digite um valor: '))
    if numero not in valores:
        valores.append(numero)
        print('Valor adicionado com sucesso...')
    else:
        print('Esse valor ja foi adicionado. Tente novamente...')

    resposta = str(input('Deseja continuar ? (S/N): ')).strip().upper()

    if resposta == 'N':
        break

valores.sort()
print('')
print('Os valores digitados foram', ', '.join(map(str, valores)))