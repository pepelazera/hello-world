from time import sleep

soma = 0
media = 0
contador = 0 
maior = None
menor = None

while True: 
    num = int(input("Digite um número: "))
    resposta = str(input("Deseja continuar (S/N) ? ")).strip().upper()

    soma += num
    contador += 1 
    media = soma / contador

    if maior is None or num > maior:
         maior = num
    
    if menor is None or num < menor:
        menor = num

    if resposta == "S":
        continue

    elif resposta == "N":
        sleep(0.4)
        print('')
        print("Programa encerrado. Carregando resultados...")
        print('')
        break


sleep(1.2)
print(f"A média de todos os números digitados é {media:.1f}")
print(f"O maior número digitado foi {maior}.")
print(f"O menor número digitado foi {menor}.")