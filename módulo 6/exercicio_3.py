lista = [1, 10, 20, 35, 22, 12]

i=0
total=0

qtd = len(lista)
while i < qtd:
    total = total + lista[i]
    i+=1

media = total // qtd

print ("A soma dos numeros digitados é:",total)
print ("A média dos números digitados é: ", media)