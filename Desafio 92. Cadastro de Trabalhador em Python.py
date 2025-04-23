informações = dict()

informações['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
informações['clt'] = int(input('Carteira de trabalho (0 caso não tenha): '))
informações['idade']= 2025 - nascimento

if informações['clt'] == 0:
    print('')
    print('-' * 30)
    print(f'- Nome do indivíduo é {informações['nome']}.')
    print(f'- Sua idade é {informações['idade']}')
    print('- Clt tem o valor 0')
else:
    informações['contratação'] = int(input('Ano de contratação: '))
    informações['salário'] = float(input('Salário: R$'))
    informações['aposentadoria'] = informações['idade'] + (informações['contratação'] + 35) - 2025
    print('')
    print('-' * 30)
    print(f'- Nome do indivíduo é {informações['nome']}.')
    print(f'- Sua idade é {informações['idade']}')
    print(f'- Clt tem o valor {informações['clt']}.')
    print(f'- Foi contratado no ano de {informações['contratação']}.')
    print(f'- Seu salário é de {informações["salário"]}.')
    print(f'- Irá se aposentar com {informações['aposentadoria']} anos.')  