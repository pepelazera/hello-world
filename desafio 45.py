from time import sleep
import random

cores = {'limpa':'\033[m',
         'roxo': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         }

while True:
    print('')
    print(f'{cores['limpa']}Suas opções: ')
    print(f'{cores['limpa']}[ 1 ] PEDRA')
    print(f'{cores['limpa']}[ 2 ] PAPEL')
    print(f'{cores['limpa']}[ 3 ] TESOURA')

    pedra = 1 
    papel = 2
    tesoura = 3

    opcoes = {1: 'PEDRA', 2: 'PAPEL', 3: 'TESOURA'}
    jogador = int(input(f'{cores['limpa']}Qual a sua jogada ? '))
    computador = random.randint(1,3)
    vencedor = pedra > tesoura > papel > pedra

    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!!')

    print('-' * 15)
    print(f'{cores['verde']}O jogador jogou {jogador}')
    print(f'{cores['roxo']}O computador jogou {computador}')
    print('-' * 15)
    print('')
    print(f'{cores['amarelo']}Processando...')
    sleep(1.4)
    print('')

    if computador == 1: #computador jogou PEDRA
        if jogador == 1:
            print(f'{cores['amarelo']}Empate')
        elif jogador == 2:
            print(f'{cores['verde']}O jogador venceu!!!')
        elif jogador == 3:
            print(f'{cores['roxo']}O computador venceu!!!')
        elif jogador != 1 or jogador != 2 or jogador != 3:
            print(f'{cores['vermelho']}JOGADA INVALIDA')

    elif computador == 2: #computador jogou PAPEL
        if jogador == 1:
            print(f'{cores['roxo']}O computador venceu!!!')
        elif jogador == 2:
            print(f'{cores['amarelo']}EMPATE')
        elif jogador == 3:
            print(f'{cores['verde']}O jogador venceu!!!')
        elif jogador != 1 or jogador != 2 or jogador != 3:
            print('JOGADA INVALIDA!!!')

    elif computador == 3: #computador jogou TESOURA
        if jogador == 1: #jogador jogou PEDRA
            print(f'{cores['verde']}O jogador venceu!!!')
        elif jogador == 2: #jogador jogou PAPEL
            print(f'{cores['roxo']}O computador venceu!!!')
        elif jogador == 3:
            print(f'{cores['amarelo']}EMPATE')
        elif jogador != 1 or jogador != 2 or jogador != 3:
            print(f'{cores['vermelho']}JOGADA INVALIDA')

    sleep(1.4)
    print('')
    repetir = str(input(f'{cores['limpa']}Deseja jogar novamente ? (s/n): ')).strip().lower()
    if repetir == 's':
        continue
    elif repetir == 'n':
        print(f"{cores['verde']}Obrigado por jogar!") 
    elif repetir != 's' or repetir != 'n':
        print(f'{cores['vermelho']}Digite (s/n) para continuar ou parar o jogo.')
        sleep(1.4)
        continue
    break