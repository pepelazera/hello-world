lista = []

while True:
    valor = lista.append(int(input('Digite um valor: ')))

    resposta = str(input('Quer continuar (S/N) ? ')).strip().upper()
    if resposta in 'Nn':
        break

elementos = len(lista)
lista.sort(reverse=True)

print(f'Você digitou {elementos} elementos.')
print('Os valores em ordem decrescente são', ', '.join(map(str, lista)))
if 5 not in lista:
    print('O número 5 não está presente na lista.')
else:
    print('O valor 5 está presente na lista.')
    