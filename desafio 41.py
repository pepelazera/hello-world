from datetime import datetime
ano = int(input('Ano de nascimento: '))
anoatual = datetime.now().year
idade = anoatual - ano
print('')
print(f'O atleta tem {idade} anos')

if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoira: JUNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
else: 
    print('Categoria: MASTER')