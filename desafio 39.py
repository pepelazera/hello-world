from datetime import datetime
ano = int(input('Ano de nascimento: '))
genero = str(input('Qual seu sexo ? ').lower())
esseano = datetime.now().year
idade = esseano - ano

if genero == 'feminino':
    print('Voce nao Precisa do alistamento militar obrigatorio')

if genero == 'masculino':
    if idade == 18:
        print('')
        print(f'Quem nasceu em {ano} tera {idade} anos em {esseano}')
        print('Seu alistamento sera esse ano')
    elif idade < 18 :
        anosfaltantes = 18 - idade
        anoalistamento = esseano + anosfaltantes
        print('')
        print(f'Quem nasceu em {ano} tem {idade} anos em {esseano}')
        print(f'Aida faltam {anosfaltantes} anos para se alistar')
        print(f'Seu alistamento sera em {anoalistamento}')
    else:
        anospasssados = idade - 18
        anoalistamento = esseano - anospasssados
        print('')
        print(f'Quem nasceu em {ano} tem {idade} anos em {esseano}')
        print(f'Voce ja deveria ter se alistado desde {anoalistamento}')
else:
    print('Erro: Gênero não reconhecido. Por favor, digite "masculino" ou "feminino".')