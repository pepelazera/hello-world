valores = []
ordenados = 0

while True:
    valor = (int(input('Digite um valor: ')))

    if valor in valores:
        print('Valor já existente, não irei adicioná-lo novamente.')
        
    else:
        valores.append(valor)
        print('Valor adiconado com sucesso...')

    ordenados = valores.sort()
    resposta = str(input('Quer continuar (S/N) ? ')).strip().upper()
    print('')
    if resposta == 'S':
        continue
    elif resposta == 'N':
        break
    else:
        print('Resposta inexistente.')
        continue

print('')
print('Você digitou os valores', ', '.join(map(str, valores)))