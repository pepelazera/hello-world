def notas(* num, sit=False):
    nt = dict()
    nt["total"] = len(num)
    nt["maior"] = max(num)
    nt["menor"] = min(num)
    nt["media"] = sum(num) / len(num)
    if sit:
        if nt["media"] >= 7:
            nt["Situação"] = "BOA"
        else:
            nt["Situação"] = "RUIM"
    return nt

#programa principal
resp = notas(7.6, 9.5, 8.7, sit=True)
print(resp)