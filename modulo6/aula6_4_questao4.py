
print()
alunos = ["Maria", "Jose", "Carla", "Sol"]
print("\nAlunos: ", alunos)
notas = [35, 50, 20, 80]
print("\nNota dos alunos: ", notas)
aprovados = [alunos[i] for i in range(len(notas)) if notas[i] >= 60]
print("\nAlunos aprovados: ", aprovados)
print()