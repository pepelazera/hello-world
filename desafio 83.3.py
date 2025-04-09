expr = str(input('Digite uma expressão: '))
lista = []

for simb in expr:
    if simb == ('('):
        lista.append('(')
    elif simb == ('('):
        if len(lista) > 0: # Indica que se o tamanho da lista for maior do que 0, a lista não está vazia 
            lista.pop() # Usa o pop para remover o último elemento da lista 
        else:    
            lista.append(')') # Caso a pilha esteja vazia ele adiciona um fechamento de parênteses 
            break

if len(lista) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
    