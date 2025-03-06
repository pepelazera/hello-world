#comeca aqui
nome = str(input('Digite seu nome completo: '))
print()

#deixa todas as letras maiusculas 
print('Seu nome em maiusculo eh:', nome.upper())
print()

#deixa todas as letras minusculas
print('Seu nome em minusculo eh:', nome.lower())
print()

#ja o len serve para ver quantas letras tem o nome 
print('Seu nome tem ao todo', len(nome), 'letras')
print()

#vai contar so ate a 4 letra, mas tem que colocar um numero a mais, ou seja, 5, pq ele sempre vai subtrair 1 no final, ou seja :5 == 4, pois fica 5-1==4
print('Seu primeiro nome eh:', nome[:5])
print()

#nesse caso eh o mesmo dos dois ultimos
print(f'Seu primeiro nome eh {nome[:5]} e ele tem {len(nome[0:5])} letras')
print()