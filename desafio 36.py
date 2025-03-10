#cores no programa
cores = {'limpa':'\033[m',
         'roxo': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         }

#variaveis que vao ser utilizadas
valor = float(input(f'{cores['amarelo']}Valor da casa: R$')) 
salario = float(input(f'{cores['amarelo']}Salario do comprador: R$'))
tempo = int(input(f'{cores['amarelo']}Quantos anos de financiamento: '))

# Calculando a prestação mensal
meses = tempo * 12  # Convertendo anos em meses
prestacao = valor / meses  # Prestação mensal
limiteprestacao = salario * 0.30

print('')
print(f'Para pagar uma conta de {valor} em {tempo} anos, a prestacao sera de {prestacao:.2f}')

#comandos do codigo
if prestacao <= limiteprestacao:
    print(f'{cores['verde']}Emprestimo APROVADO!')
else:
    print(f'{cores['vermelho']}Emprestimo NEGADO!')
