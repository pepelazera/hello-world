salario = float(input('Qual eh o salario do funcionario ? R$'))

if salario > 1250: 
    salario1 = salario + (salario * 10 / 100)
    print(f'Quem ganhava {salario:.2f}, agora vai ganhar {salario1:.2f}')

if salario < 1250:
    salario2 = salario + (salario * 15 / 100) 
    print(f'Quem ganhava {salario:.2f}, agora vai ganhar {salario2:.2f}')

if salario == 1250: 
    print(f'O salario continuara sendo {salario}')