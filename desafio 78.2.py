lista = []

for n in range(0, 5):
    numero = int(input(f'Digite um número para a posição {n}: '))
    lista.append(numero)


posicaomaior = lista.index(max(lista))
posicaomenor = lista.index(min(lista))
print('Você digitou os valores', ' '.join((map(str, lista))))
print(f'O maior valor digitado foi {max(lista)} na posição {posicaomaior}.')
print(f'O menor valor digitado foi {min(lista)} na posição {posicaomenor}.')