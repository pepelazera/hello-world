from uteis import numeros

num = int(input("Digite um valor: "))
fat = numeros.fatorial(num)
print(f"O fatorial de {num} é {fat}.")
print(f"O dobro é {numeros.dobro(num)} e o triplo é {numeros.triplo(num)}.")