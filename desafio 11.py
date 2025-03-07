cores = {'limpa':'\033[m',
         'roxo': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         }

largura = float(input(f'{cores['amarelo']}Largura da parede: '))
altura = float(input(f'{cores['amarelo']}Altura da parede: '))
area = (largura * altura)
litro = (area/2)
print('{}Sua parede tem a dimensao de {}x{} e sua area eh {}m2'.format(cores['verde'],largura, altura, area))
print('{}Para pintar essa parede, vai precisar de {}L de tinta.'.format(cores['verde'],litro))