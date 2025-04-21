lista = []

while True:
    nome = str(input('Nome: '))
    n1 = int(input('Nota 1: '))
    n2 = int(input('Nota 2: '))
    media = (n1 + n2) / 2
    lista.append([nome, [n1, n2], media])

    resp = str(input('Deseja continuar (S/N): ')).strip().upper()
    if resp == 'N':
        break

print('')
print('-' * 30)
print('No.  NOME        MÉDIA')

for i, a in enumerate(lista):
    print(f'{i:<5}{a[0]:<13}{a[2]:<2}')
print('-' * 30)

while True:
    print('')
    opcao = int(input('Mostrar nota de qual aluno ? (999 interrompe): '))

    if opcao == 999:
        print('Finalizando...')
        break
    if opcao <= len(lista) -1:
        print(f'As notas de {lista[opcao][0]} são {lista[opcao][1]}')