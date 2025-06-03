with open("arquivos.txt", "r") as arq:
    print(next(arq))
    print(next(arq)) # Traz sempre o próximo

#read: le o arquivo.txt da maneira que foi escrito
# readlines: le linha por linha, como se fosse uma lista
# rb: Le a string em bites/binário
# print(x.decode()) Decodifica de bites para string automáticamente 