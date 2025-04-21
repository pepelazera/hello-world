ficha = []


while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])

    resp = str(input('Quer continuar ? (S/N): ')).strip().upper()
    if resp == 'N':
        break

print('')
print('-=' * 30)
print('')
print('No.', end='      ')
print('NOME', end='     ')
print('MÉDIA    ')
print('-' * 30)

for i, a in enumerate(ficha):
    print(f'{i:<9}{a[0]:<10}{a[2]:>}')
print('-' * 30)

while True:
    print('')
    opcao = int(input('Deseja mostrar as notas de que aluno ? (999 interrompe): '))
    if opcao == 999:
        print('Finalizando....')
        break
    if opcao <= len(ficha) - 1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
print('')