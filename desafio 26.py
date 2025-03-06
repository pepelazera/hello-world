#variaveis
frase = str(input('Digite uma frase: ')).strip().upper()

#comandos
contarletra = frase.count('A')
acharletra = frase.find('A') + 1
acharletra2 = frase.rfind('A') + 1


#prints 
print(f'A letra \'A\' aparece {contarletra} vezes')
print(f'A primeira letra \'A\' apareceu na posicao {acharletra}')
print (f'A ultima letra \'A\' aparece na posicao {acharletra2}')