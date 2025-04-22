from random import sample
from operator import itemgetter
from time import sleep

valores = sample(range(1, 7), 4)

jogadores = {"Jogador 1: ": valores[0],
             "Jogador 2: ": valores[1],
             "Jogador 3: ": valores[2],
             "Jogador 4: ": valores[3]
             }
ranking = list()

print('Valores sorteados: ')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True) # o itemgetter vai capturar um item dentro da estrutura da lista
print()
print('-' * 30)
print(' == RANKING DOS JOGADORES ==')

for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} {v[1]}.')
    sleep(1)