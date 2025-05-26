# Mode
# r - Leitura
# a - Append/Incrementar
# w - Write 
# x - Criar Arquivo
# r+ - Leitura + Escrita

arquivo = open("AulaArq/teste3.txt", "x") # Caso use o W, ele irá limpar o arquivo anterior e escrever do zero, já o A ele faz uma continuação escrevendo logo abaixo

print(arquivo.readable()) # Verifica se o arquivo pode ser lido
print(arquivo.read()) # Le todas as linhas do arquivo
print(arquivo.readline()) # Le a primeira linha do arquivo, e caso coloque outros readline ele lerá as linhas sucetivas
print(arquivo.readlines())

arquivo.write("python\n")

arquivo.close()

import os

if os.path.exists("AulaArq/teste2.txt"):
    os.remove("AulaArq/teste2.txt") 
else:
    print("Arquivo não existe.")

os.rmdir("AulaArq/nova_pasta")
