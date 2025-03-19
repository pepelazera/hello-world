#Variáveis
idademaior = -1
idademenor = float('inf')
maisvelho = None
maioridade = -1
somaidades = 0
totalmulher20 = 0

#Lista de dados
pessoas = []

#Dados de 4 pessoas
for count in range(1, 5):
    nome = input('Digite seu nome: ').strip().lower()
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo (masculino/feminino): ').strip().lower()

    pessoas.append({'nome': nome, 'idade': idade, 'sexo':sexo})
    somaidades += idade

    #Calculando maior ou menor de idade
    if idade > idademaior:
        idademaior = idade
    if idade < idademenor:
        idademenor = idade

#Calculando média das idades
media = somaidades / len(pessoas)
print('')
print(f'A média das idades é {media:.2f}')

maisvelho = None
maioridade = -1 
totalmulher20 = 0

#Procurando homem mais velho
for pessoa in pessoas:
   if pessoa['sexo'] in 'masculino' and pessoa['idade'] > maioridade:
       maisvelho = pessoa['nome']
       maioridade = pessoa['idade'] 

   if pessoa['sexo'] in 'feminino' and pessoa['idade'] < 20:
      totalmulher20 += 1

#Print homem mais velho
if maisvelho:
    print(f'O homem mais velho é {maisvelho}, com {maioridade} anos.')
else:
    print('Nenhum homem encontrado.')

#Print mulheres com menos de 20 anos
print('')
print(f'Nessa lista existem {totalmulher20} mulheres com menos de 20 anos.')