from random import sample
from operator import itemgetter
from time import sleep

valores = sample(range(1, 7), 4)

jogadores = {
    "jogador 1: ": valores[0],
    "jogador 2: ": valores[1],
    "jogador 3: ": valores[2],
    "jogador 4: ": valores[3]
}
ranking = list()

print('')
print('Valores sorteados: ')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True) # o itemgetter vai capturar um item dentro da estrutura da lista

print()
print('-' * 30)
print(' == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} {v[1]} no dado.')
    sleep(1)