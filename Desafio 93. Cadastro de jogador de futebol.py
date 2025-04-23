dados = dict()
quantgols =  list()

dados['nome'] = str(input('Nome do jogador: '))
dados['partidas'] = int(input(f'Quantas partidas {dados['nome']} jogou ? '))

for p in range(dados['partidas']):
   quantgols.append(int(input(f'Quantos gols na partida {p+1} ? ')))
   dados['total'] = sum(quantgols)

print('')
print(dados.items(), quantgols)
print('')


for k, v in dados.items():
   print(f'O campo {k} tem valor {v}.')
print(f'O campo gols tem valor {quantgols}.')


print('')
print(f'O jogador {dados['nome']} jogou {dados['partidas']} partidas.')
for p, g in enumerate(quantgols):
   print(f'    => Na {p+1}a. partida, fez {g} gols.')

print('')
print(f'Foi um total de {dados['total']} gols.')