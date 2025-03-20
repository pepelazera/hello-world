import random
from time import sleep

while True:
    numerosorteado = random.randint(0, 10)

    tentativas = 0

    numero = int(input('Vou pensar em um numero de 0 a 10. Tente advinhar... '))
    print('')
    print('Processando...')
    sleep(1.2)
    print('')

    while numero != numerosorteado:
        tentativas += 1 
        print('Você errou, tente mais uma vez!')
        numero = int(input(''))

    tentativas += 1
    print('Parabéns, você acertou! Você precisou de {} tentativa/tentativas para chegar a resposta correta.'.format(tentativas))

    jogardenovo = input('Você gostaria de jogar novamente? (s/n): ').strip().lower()
    if jogardenovo != 's':
        print('')
        print('Verificando resposta...')
        sleep(1.2)
        print('Obrigado por jogar! Até a próxima!')
        break 