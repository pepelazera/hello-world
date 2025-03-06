print('Analisador de triangulos')
print('')

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('É possível formar um triângulo com esses valores.')
else: 
    print('Não é possível formar um triângulo com esses valores.')