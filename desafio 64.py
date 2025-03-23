from time import sleep
contador = 0
soma = 0

while True:
    num = int(input("Digite um número (999 para parar o programa): "))

    if num == 999:
        print('')
        print("Programa encerrado.")
        sleep(0.5)
        break

    contador += 1 
    soma += num 

print('')
print("Carregando resultados...")
sleep(1.2)
print('')
print(f"Você digitou {contador} números antes de encerrar o programa.")
print(f"A soma entre esses números é {soma}")