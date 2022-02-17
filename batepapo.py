alunos = [
    { 
        "nome": "Alice",
        "nota": 10,
    },
    { 
        "nome": "Bob",
        "nota": 8,
    }    
    
]

alunos_nota_10 = [aluno for aluno in alunos if aluno["nota"] == 10]
#alunos_nota_10 = []

#for aluno in alunos: # {"nome":"...","nota":...}
#   if aluno["nota"] == 10:
#      alunos_nota_10.append(alunos)


print(alunos)
print(alunos_nota_10)

# numeros = [1,2,5,6,8,10,13,17,20,22]
# numeros_pares = []

#for i in numeros:
#    if i%2 == 0:
#        numeros_pares.append(i)

# numeros_pares = [i for i in numeros if i%2 ==0] #equivalente ao anterior

# print("Lista de numeros:", numeros)
# print("Lista de números pares:", numeros_pares)