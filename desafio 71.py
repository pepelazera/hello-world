from time import sleep

print("-" * 30)
print("         BANCO CEV      ")
print("-" * 30)

cedula100 = cedula50 = cedula10 = cedula5 = 0
cont = 0

while True:
    saque = int(input("Que valor você quer sacar ? "))
    print("Imprimindo....")
    print("")
    sleep(1.2)

    if saque <= 0:
        print("Impossível sacar esse valor. Por favor, escolha um valor válido.")
        print('')

    if saque >= 100:
        cedula100 = saque // 100
        saque = saque % 100
        print(f"Total de {cedula100} cédulas/cédula de R$100")

    if saque >= 50:
        cedula50 = saque // 50
        saque = saque % 50
        print(f"Total de {cedula50} cédulas/cédula de R$50")
    
    if saque >= 10:
        cedula10 = saque // 10
        saque = saque % 10
        print(f"Total de {cedula10} cédulas/cédula de R$10") 

    if saque >= 5:
        cedula5 = saque // 5
        saque = saque % 5
        print(f"Total de {cedula5} cédulas/cédula de R$5")

    if saque > 0:
        print(f'Não é possível sacar o valor restante de R${saque}')
    
    print("")
    continuar = str(input("Deseja sacar mais algum valor (S/N)) ? ")).strip().upper()
    print("Processando...")
    sleep(1.2)

    if continuar == "S":
        print("")
        print("Reiniciando programa...")
        print("")
        sleep(1.2)
    elif continuar == "N":
        print("")
        print("Volte sempre ao BANCO CEV.Tenha um bom dia!")
        break
    else:
        print("Selecione caractéres válidos.")
        print("")
        print("Reiniciando caixa...")
        print("")
        sleep(1.5)