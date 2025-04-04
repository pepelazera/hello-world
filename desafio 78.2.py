valores = []

for count in range(1,6):
    valores.append(int(input(f'Digite um valor na posição {count}: ')))

maiorvalor = max(valores)
menorvalor = min(valores)

posicaomaior = []
for c, v in enumerate(valores):
    if maiorvalor == v:
        posicaomaior.append(c+1)

posicaomenor = []
for c, v in enumerate(valores):
    if menorvalor == v :
        posicaomenor.append(c+1)

print('-=' * 20)
print('Você digitou os valores',', '.join(map(str, valores)))
print(f'O maior valor foi {maiorvalor}, encontrado na posição', ', '.join(map(str, posicaomaior)))
print(f'O menor valor foi {menorvalor}, encontrado na posição', ', '.join(map(str, posicaomenor)))