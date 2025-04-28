dados = dict()
time = list()

while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador: '))
    dados['partidas'] = int(input(f'Quantas partidas {dados['nome']} jogou ? '))
    quantgols = list()

    for p in range(dados['partidas']):
        quantgols.append(int(input(f'Quantos gols na partida {p+1} ? ')))
    dados['total'] = sum(quantgols)
    dados['gols'] = quantgols[:]
    time.append(dados.copy())
    while True:
        resp = str(input('Deseja continuar ? (S/N): ')).strip().upper()
        if resp in 'SN':
            break
        else:
            print('ERRO!')
            continue
    if resp == 'N':
        break

print('')
print('-' * 50)
print('cod ', end='')
for k in dados.keys():
    print(f'{k:<15}', end='')
print('')
print('-' * 50)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for p in v.values():
        print(f'{str(p):<15}', end='')
    print('')
while True:
    resp2 = int(input('Você quer informações de qual jogador ? (999 para parar): '))

    if resp2 == 999:
        break
    if resp2 >= len(time):
        print(f'ERRO! Não existe jogador com código {resp2}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[resp2]["nome"]}--')
        for j, g in enumerate(time[resp2]["gols"]):
            print(f'No jogo {j+1} fez {g} gols.')