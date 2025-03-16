frase = str(input('Digite seu frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'A palavra {frase} ao contrário é {inverso}')
    print('Temos um polídromo!')
else:
    print(f'A palavra {frase} ao contrário é {inverso}')
    print('A frase não é um polídromo')