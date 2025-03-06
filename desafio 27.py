#variaveis iniciais
n= str(input('Digite seu nome completo:')).strip()
nome = n.split()

#print
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome eh {nome[0]}')
print('Seu ultimo nome eh {}'.format(nome[len(nome) - 1 ]))