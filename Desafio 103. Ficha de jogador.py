def ficha(jog="<desconhecido>", gol=0):
    """
     -> Def irá ter um valor para jog e para gol, assim evitando o erro do código;
      - O valor isnumeric do programa principal irá transformar a string utilizada anteriormente em um valor inteiro caso seja digitado um número;
      - Os if e else do código servem para evitar que erros aconteçam caso o usuário esqueça ou erre alguma informação digitada. Caso o usuários escreva o número por extenso, ele não será entendido como um número.

    """
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

# Programa principal
n = str(input('Nome do jogador: '))
g = str(input('Quantidade de gols: '))
if g.isnumeric():
    int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
help(ficha)