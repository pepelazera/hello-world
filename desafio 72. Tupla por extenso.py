from time import sleep

cont = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 
    'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte']

while True:
    numero0a20 = int(input('Digite um número entre 0 a 20: '))

    if numero0a20 < 0 or numero0a20 > 20:
        print('Por favor, digite números válidos.\n')
        print('')
        continue

    print(f'Você digitou o número {cont[numero0a20]}.')


#Loop para garantir que o usuário insira uma resposta válida
    while True:
        resposta = str(input('Deseja continuar (S/N) ? ')).strip().upper()

        if resposta == 'S':
            print('\nReiniciando programa...\n')
            print('')
            sleep(1.3)
            break  # Sai do loop de validação e reinicia o programa
        elif resposta == 'N':
            sleep(1.3)
            print('Por hoje é só! Muito obrigado!')
            exit() # Sai completamente do programa
        else:
            print('Opção inválida! Digite apenas S ou N.')
            print('')
            sleep(0.5)
            continue