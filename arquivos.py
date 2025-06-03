arq = open("arquivinho.txt", "w")

x = ["Pedro", "Joao","Marcos", "Carlos"]

for nome in x:
    arq.write(nome + "\n")

arq.close()