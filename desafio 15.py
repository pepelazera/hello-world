dias = int(input('Quantos dias alugados ? '))
km = float(input('Quantos km rodados ? '))
valorfinal = ((60 * dias) + (0.15 * km)) 
print('O total a pagar eh de R${:.2f}'.format(valorfinal))