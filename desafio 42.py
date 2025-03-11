from time import sleep
print('Analisador de triangulos')
print('')

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

print('Processando...')
sleep(1.4)
print('')

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('É possível formar um triângulo ', end='')
    if s1 == s2 == s3:
        print('EQUILATERO')
    elif s1 != s2 != s3 != s1: 
        print('ESCALENO')
    else:
        print('ISOCELES')
else: 
    print('Esses valores nao podem ser formado um triangulo com esses valores.')