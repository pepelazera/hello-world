pessoas = []
pesos = []
maiorpeso = float('-inf')
menorpeso = float('inf')

while True:
    pessoa = str(input('Nome: '))
    pessoas.append(pessoa)
    peso = float(input('Peso: '))
    pesos.append(peso)

    resposta = str(input('Quer continuar ? (S/N): ')).strip().upper()

    if peso > maiorpeso:
        maiorpeso = peso
    elif peso < menorpeso:
        menorpeso = peso
    
    if resposta != 'N':
        print('')
        continue
    else:
        break

indicemaiorpeso = pesos.index(maiorpeso)
nomemaiorpeso = pessoas[indicemaiorpeso]
indicemenorpeso = pesos.index(menorpeso)
nomemenorpeso = pessoas[indicemenorpeso]

totpessoas = len(pesos)
print(f'Foram registrada {totpessoas} pessoas')
print(f'O maior peso registrado foi {maiorpeso} Kg e foi de {nomemaiorpeso}')
print(f'O menor peso registrado foi {menorpeso} Kg e foi de {nomemenorpeso}')