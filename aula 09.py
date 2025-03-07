frase = 'Curso em Video Python'
dividido = frase.split()

# Definindo códigos de cores ANSI
cores = [
    '\033[31m',  '\033[32m'
]

# Código para resetar a cor
RESET = '\033[0m'

# Imprimindo cada palavra com uma cor diferente
for i, palavra in enumerate(dividido):
    print(f"{cores[i % len(cores)]}{palavra}{RESET}")