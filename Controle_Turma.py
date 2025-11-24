aluno01 = ("Ana", 17, 9.3)
aluno02 = ("Pedro", 18, 8.4)
aluno03 = ("Maria", 17, 9.8)

turma = list()
turma.append(aluno01)
turma.append(aluno02)
turma.append(aluno03)

for c in range(len(turma)):
    print(f"{turma[c]}")