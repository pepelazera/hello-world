valores = []

for count in range(1,6):
    valores.append(int(input(f'Digite um valor na posição {count}: ')))

maiorvalor = max(valores)
menorvalor = min(valores)

posicaomaior = []
for i, v in enumerate(valores):
    if v == maiorvalor:
        posicaomaior.append(i+1)

posicaomenor = []
for i, v in enumerate(valores):
    if v == menorvalor:
        posicaomenor.append(i+1)


print('-=' * 20)
print('')
print('Você digitou os valores', ' '.join(map(str, valores)))
print(f'O maior valor encontrado foi {maiorvalor} na posição', ', '.join(map(str, posicaomaior)))
print(f'O menor valor encontrado foi {menorvalor} na posição', ', '.join(map(str, posicaomenor)))