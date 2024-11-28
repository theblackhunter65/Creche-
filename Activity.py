# compra = ["Arroz",
#           "Feijão",
#            "Carne",
#            "Pão"]
# for x in compra:
#     print(x)
notas = []
aluno = []
for y in range (1,11,1):
    y = input("Escreva o nome do aluno:")
    nota = float(input("digite a nota:"))
    notas.append(nota)
    aluno.append(y)
media = sum(notas) / len(notas)
print(f"A média das notas é: {media:.2f}")
print(media)
plus = max(notas)
print(plus)
aluno_max = aluno[notas.index(plus)]
min = min(notas)
print(min)
aluno_min = aluno[notas.index(min)]
print(f"O aluno com a maior nota é {aluno_max}, com nota {plus}.")
print(f"O aluno com a menor nota é {aluno_min}, com nota {min}.")
