#lembrar de usar o STR quando tiver esse tipo de desafio que envoolva strip, upper, lower, count, find, etc...
c = str(input('Qual a sua cidade ? ')).strip()

#comandos de [:5] quer dizer que vai mostrar do valor zero ate o 5, que nesse caso forma a palavra abaixo. 
print(c[:5].upper() == 'SANTO')