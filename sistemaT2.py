import random

voos = {
    '001': {'destino': 'Siria', 'assentos': 10},
    '002': {'destino': 'Alabama', 'assentos': 12},
    '003': {'destino': 'Emirados Arabes', 'assentos': 14},
}

reservas = []

def gerar_Reserva():
    return str(random.randint(10000, 999999)) # str ou String = palavra


def fazer_reserva(nome, numero_voo, classe):
    while True:
        if numero_voo not in voos:
            print("ERRO: voo nao encontrado.")
            return

        elif classe not in "economica".strip().upper() and classe not in "econômica"\
                and classe not in "executiva".strip().upper() and classe not in "primeira classe".strip().upper():
            print("ERRO: Classe inexistente.")
            return

        elif voos[numero_voo]['assentos'] <= 0:
            print("Sem assentos disponiveis.")
            return

        else:
            codigo = gerar_Reserva()
            reserva = {
                "codigo": codigo,
                "nome": nome,
                "voo": numero_voo,
                "destino": voos[numero_voo]["destino"],
                "classe": classe
            }

            reservas.append(reserva)
            voos[numero_voo]["assentos"] -= 1

            print(f"Nome do passageiro: {nome}\n"
                  f"Numero do voo: {numero_voo}\n"
                  f"Classe: {classe}\n"
                  f"Codigo: {codigo}")
            break



def cancelar_reserva(codigo):
    for reserva in reservas:
        if reserva["codigo"] == codigo:
            reservas.remove(reserva)
            voos[reserva["voo"]]["assentos"] += 1
            return "Reserva cancelada com sucesso!"
    return "Codigo nao encontrado."


def listar_reservas():
    return reservas


def listar_voos():
    return voos


def cadastrar_voo(num_voo, destino):
    """
    Cadastra um novo voo no sistema.

    """

    if num_voo in voos:
        return f"Erro: O voo {num_voo} já está cadastrado."

    try:
        num_assentos = random.randint(10, 15)
    except (ValueError, TypeError):
        return "Erro: A quantidade de assentos deve ser um número."

    voos[num_voo] = {'destino': destino, 'assentos': num_assentos}

    return f"Voo {num_voo} para {destino} ({num_assentos} assentos) cadastrado com sucesso!"
