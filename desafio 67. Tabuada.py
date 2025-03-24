from time import sleep

#looping para
while True:   
    print("")
    num = int(input("Quer ver a tabuada de qual valor ? "))
    print("")
    print("Processando...")
    sleep(1.2)
    print("")
    if num < 0:
        break
    print("-" * 30)

    for count in range(1, 11):
        print(f"{num} * {count} = {num*count}")

    print("-" * 30)

print("Programa encerrado. Obrigado e volte sempre que quiser!")