valores = []
for count in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores): # faz interação sobre uma sequência
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')