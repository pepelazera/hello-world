num = [2, 5, 9, 1]
num[2] = 3
num.append(7) # Usado pra adicionar os valores que você digitar na lista.
num.sort() # Coloca os números em ordem
num.insert(2, 2) # Adiciona um elemento em uma posição específica
print(num)
print(f'Essa lista tem {len(num)} elementos.')
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4.')