import time
while True:
     while True:
          a = (input('Digite o primeiro valor: '))
          b = (input('Digite o segundo valor: '))

          try:
               a = float(a)
               b = float(b)
          except ValueError:
               print('Operação inválida. Por favor, insira uma operação matemática válida.')
               continue
          break

     while True:

               operacao = input('Escolha a operação (+, -, *, /): ')
               if operacao not in ('+', '-', '*', '/'):
                  print('Operação inválida. Por favor, insira uma operação matemática válida.')
                  continue
               break
     
     if operacao == '+':
      resultado = a + b

     if operacao == '-':
      resultado = a - b 

     if operacao == '*':
      resultado = a * b   

     if operacao == '/': 
          if b == 0:
               print('Operação inválida. Por favor, insira uma operação matemática válida.')
               continue
          else:
                    resultado = a / b

     print(resultado)

     repeat = input('Deseja realizar outra operação ? (s/n):', )
     if repeat == 's':
               print('')
               print('Reininciando...')
               time.sleep(2)

     if repeat == 'n':
               print('')
               print('Processando...')
               time.sleep(2)
               print('')
               print('Encerramos por aqui. Obrigado!')
     