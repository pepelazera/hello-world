expr = str(input('Digite uma expressão: '))
lista = []

for simb in expr:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0: # Essa expressão significa que cada parêntese que abriu teve sua relação com o parêntese que fechou, sem nenhum estar incompleto
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')