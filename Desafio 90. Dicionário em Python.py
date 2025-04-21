aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))

print('-' * 30)
print(f'- Nome é {aluno['nome']}')
print(f'- A sua média é {aluno['media']}')

if aluno['media'] >= 7:
    print(f'- {aluno['nome']} está aprovado.')
elif aluno['media'] < 7:
    print(f'- {aluno['nome']} está de recuperação.') 