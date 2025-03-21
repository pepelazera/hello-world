from time import sleep

while True:
    print("-=" * 10)
    print("Gerador de PA")
    print("-=" * 10)
    primeiro = int(input("Primeiro termo: "))
    razao = int(input("Razão da PA: "))
    termo = primeiro 
    cont = 1
    print("")

    while cont <= 10:
        print(f"{termo} → ", end='')
        termo += razao
        cont += 1
    print("FIM")

    print("")
    resposta = str(input("Deseja refazer com outros valores (S/N) ? ")).strip().upper()
    print("Processando...")
    sleep(1.2)

    if resposta == "S":
        print("")
        print("Reiniciando...")
        sleep(1.2)
        print("")
    elif resposta == "N":
        print("")
        print("Por hoje é só. Obrigado por testar esse programa!")
        break
