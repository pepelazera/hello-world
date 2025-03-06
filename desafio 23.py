#Variaveis 
num = int(input('Digite um número: '))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

#Comandos de aplicacao
print(f'Analisando o número {num}...') 
print(f'unidade: {u}')
print(f'dezena: {d}')
print(f'centena: {c}')
print(f'milena: {m}')
