from math import factorial

while True:
    print('')
    print("Digite um número para")
    num = int(input("Calcular seu Fatorial: "))
    resultado = factorial(num)

    print(f"Calculando {num}!")
    print(f"Resultado = {resultado}")
    final = str(input("Deseja testar outro número (S/N) ? ")).strip().upper()
    print("Processando")
    if final == 'S':
        print('Reiniciando...')
    elif final == 'N':
        print('')
        print('Por hoje é só. Muito obrigado!')
        break