stock = {"mouse": 10, "keyboard": 5}

for item, quant in stock.items():
    print(f"We have {quant} unities of {item}")

print()

for item, quant in stock.values() and stock.items():
    print(quant, end=' ')
    print(item)