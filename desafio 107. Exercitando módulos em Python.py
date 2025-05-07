import modulo_107


num = int(input("Digite o preço: R$"))
print(f"A metade de {num} é {modulo_107.metade(num)}")
print(f"O dobro de {num} é {modulo_107.dobro(num)}")
print(f"Aumentando 10%, temos {modulo_107.aumento10(num)}.")