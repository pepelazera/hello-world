print('-' * 35)
print('     LISTAGEM DE PREÇOS      ') #This print say: "list of prices" or "price list" in Portguese 
print('-' * 35)

itens = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('....................R$   '.join(map(str, itens[0:2]))) #pencil with price
print('.................R$    '.join(map(str, itens[2:4]))) #eraser with price
print('..................R$   '.join(map(str, itens[4:6]))) #notebook with price
print('...................R$   '.join(map(str, itens[6:8]))) #case with price
print('.............R$    '.join(map(str, itens[8:10]))) #protactor with price
print('.................R$   '.join(map(str, itens[10:12]))) #compass with price
print('..................R$ '.join(map(str, itens[12:14]))) #bag with price
print('..................R$   '.join(map(str, itens[14:16]))) #pens with price
print('....................R$   '.join(map(str, itens[16:18]))) #books with price

print('-' * 35) #This prints are some lines that I put at the beginning and at the end of the program