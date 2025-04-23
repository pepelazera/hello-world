from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year-nascimento
dados['Clt'] = int(input('Carteira de trabalho (0 caso não tenha): '))

if dados['Clt'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Salário: '))
    dados['Aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('')
print('-' * 30)

for k, v in dados.items():
    print(f'- {k} tem o valor {v}.')