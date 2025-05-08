import modulo_107

num = int(input("Digite o preço: R$"))
print(f"A metade de {modulo_107.moeda(num)} é {modulo_107.metade(num, True)}")
print(f"O dobro de {modulo_107.moeda(num)} é {modulo_107.dobro(num, True)}")
print(f"Aumentando 10%, temos {modulo_107.aumentar(num, 10, True)}.")
print(f"Reduzindo 13%, temos {modulo_107.diminuir(num, 13, True)}")