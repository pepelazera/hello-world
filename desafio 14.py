cores = {'limpa':'\033[m',
         'roxo': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         }

celcius = float(input(f'{cores['amarelo']}Informe a temperatura em ºC:'))
fahrenheit = (celcius *9/5 + (32))
print('{}A temperatura de {}ºC corresponde a {:.2f}°F'.format(cores['roxo'], celcius, fahrenheit))