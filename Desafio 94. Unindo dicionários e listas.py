dados = list()
fichas = dict()
soma = media = 0

while True:
    fichas.clear()
    while True:
        nome = input('Nome: ').strip()
        if nome.replace(" ", "").isalpha():
            fichas['nome'] = nome
            break
        else:
            print('ERRO! Por favor, digite um nome válido.')

    try:
        fichas['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
        if fichas['sexo'] not in ('M', 'F'):
            input('ERRO! Por favor, digite M ou F: ')

    except ValueError:
        input('Selecione somente M ou F! ')

    fichas['idade'] = int(input('Idade: '))
    soma += fichas['idade']
    dados.append(fichas.copy())

    while True:
        resp = str(input('Deseja continuar ? (S/N): ')).strip().upper()
        if resp == 'S':
            break
        elif resp == 'N':
            break
        else:
            print('ERRO! Por favor, digite S ou N para continuar.')
    if resp == 'N':
        break

media = soma / len(dados)
print('')
print('-' * 40)
print(f'Ao todo temos {len(dados)} pessoas cadastradas.')
print(f'A média das idades é de {media:5.2f} anos.')
print(f'As mulheres cadastradas foram', end=': ')
for f in dados:
    if f['sexo'] == 'F':
        print(f'{f["nome"]}', end='  ')
print()
print(f'Listas das pessoas que estão acima da média: ', end='')
for p in dados:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
