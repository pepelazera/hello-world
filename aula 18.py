teste = []
teste.append('Gustavo')
teste.append(40)

galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = '22'
galera.append(teste[:]) # O [:] define que a lista é uma cópia 
print(galera)