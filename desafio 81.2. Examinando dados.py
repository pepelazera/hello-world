lista = []

while True:
    lista.append(int(input('Digite um valor: ')))

    resposta = str(input('Quer continuar ? (S/N): ')).strip().upper()

    if resposta == 'N':
        break
    else:
        continue

lista.sort(reverse=True)
print('')
print(f'Você digitou {len(lista)} elementos.')
print('Os valores em ordem descrescente foram', ', '.join(map(str, lista)))

if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')