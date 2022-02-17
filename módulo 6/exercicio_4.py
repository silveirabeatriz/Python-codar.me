# Alunos e suas respectivas notas
alunos = [
("Alice", 8),
("Bob", 7),
("Carlos", 9),
]

soma= 0

for aluno in alunos:
    soma = soma + aluno[1]

media = soma /len(alunos)

print (alunos)
print ("A media das notas somadas é: ",media)