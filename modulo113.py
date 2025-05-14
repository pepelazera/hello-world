def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido.")
            continue
        except KeyboardInterrupt:
            print("\033[33mAVISO: o usuário não digitou nenhum valor inteiro.")
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número real válido.")
        except KeyboardInterrupt:
            print("\033[33mAVISO: o usuário não digitou nenhum valor real.")
            return 0
        else:
            return n