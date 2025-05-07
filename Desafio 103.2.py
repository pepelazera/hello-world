def ficha(jog="<desconhecido", gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


j = str(input("Nome do jogador: "))
g = str(input("Quantidade de gols: "))
if g.isnumeric():
    int(g)
else:
    g = 0
if j.strip() == '':
    ficha(gol= g)
else:
    ficha(j, g)