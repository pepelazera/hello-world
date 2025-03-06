nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()

print('Prazer em te conhecer!')
print(f'Seu primeiro nome eh {n[0]}')
print(f'Seu ultimo nome eh {n[len(n) - 1]}')