# Mode
# r - Leitura
# a - Append/Incrementar
# w - Write
# x - Criar Arquivo
# r+ - Leitura + Escrita


#arquivo = open("mensagem.txt", "r")
#msg = arquivo.read()
#arquivo.close()
#print(msg)

caminho = "mensagem.txt" #Nesse caso, não precisa fechar o arquivo, ele já fecha automaticamente.
#with open (caminho,"r") as arq:
#    m = arq.read()
#print("-"*10)
#print(m)

msg = "A nota de matematica foi 9"
arquivo = open("mensagem.txt", "w")
arquivo.write(msg)
arquivo.close()

#adicionando de forma "fake"
with open(caminho) as arq:
    conteudo = arq.read()
conteudo = conteudo + "\nA nota de historia foi 9,7"
with open(caminho, "w") as arq:
    arq.write(conteudo)