dados = dict()
time = list()

while True:
    dados['nome'] = str(input('Nome do jogador: '))
    dados['partidas'] = int(input(f'Quantas partidas {dados['nome']} jogou ? '))

    quantgols = list()

    for p in range(dados['partidas']):
       quantgols.append(int(input(f'Quantos gols na partida {p+1} ? ')))
    dados['total'] = sum(quantgols)
    dados['gols'] = quantgols[:]
    while True:
        resp = str(input('Deseja continuar ? (S/N): ')).strip().upper()
        time.append(dados.copy())
        if resp in 'SN':
            break
        else:
            print('ERRO!')
    if resp == 'N':
        break

print('')
print('-'*40)
print('cod ', end='')
for p in dados.keys():
    print(f'{p:<13}', end='')
print('')
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:<3}', end='')
    for d in v.values():
        print(f'{str(d):<14}', end='')
    print('')
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador ? (999 para parar): '))

    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('')
print('Volte sempre!')