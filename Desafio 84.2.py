nome = []
peso = []

maiorpeso = float('-inf')
menorpeso = float('inf')

while True:
    pessoa = str(input('Nome: '))
    nome.append(pessoa)
    massa = float(input('Peso: '))
    peso.append(massa)

    if massa > maiorpeso:
        maiorpeso = massa
    elif massa < menorpeso:
        menorpeso = massa

    resp = str(input('Quer continuar ? (S/N): ')).strip().upper()

    if resp == 'N':
        break

maiorpesoencontrado = peso.index(maiorpeso)
pessoamaiorpeso = nome[maiorpesoencontrado]
menorpesoencontrado = peso.index(menorpeso)
pessoamenorpeso = nome[menorpesoencontrado]

print(f'Ao todo, foram cadastradas {len(nome)} pessoas')
print(f'O maior peso registrado foi de {maiorpeso} Kg e foi de {pessoamaiorpeso}.')
print(f'O menor peso registrado foi de {menorpeso} Kg e foi de {pessoamenorpeso}.')