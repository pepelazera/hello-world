#criar variaveis
nome = str(input('Qual seu nome completo ? ')).strip()

#comandos
print('Seu nome tem {} ? '.format(nome[16:22]), end= '')
print(nome[16:22].upper() == 'LAZERA')