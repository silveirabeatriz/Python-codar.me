lista = [1, 10, 20, 35, 22, 12]
soma=0

for num in lista:
    soma += num

print (lista)
print ("O total dos números da lista é:",soma)


#lendo números

lista = []

print ("Para encerrar digite 0.")
while num != 0:
    num = int (input("Digite os números para ser calculado:\n"))
    if (num != 0):
        lista.append(num)
soma = 0

for numero in lista:
    soma+=numero

print ("Soma dos números digitados é: ", soma)