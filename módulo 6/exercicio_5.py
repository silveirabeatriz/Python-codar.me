# Alunos e suas notas representados por dicionarios

alunos = [
{
"nome": "Alice",
"nota": 8,
},
{
"nome": "Bob",
"nota": 7,
},
{
"nome": "Carlos",
"nota": 9,
}
]

soma= 0

for aluno in alunos:
    soma +=aluno["nota"]

media = soma /len(alunos)

print ("A media das notas somadas é: ",media)