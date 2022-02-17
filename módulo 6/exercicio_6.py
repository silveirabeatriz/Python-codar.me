num = int(input("Para encerrar a insercao de números digite 0. Digite um numero inteiro:"))

lista = []

while num!=0:
    lista.append(num)
    num = int(input ("Digite um novo número:"))

print(lista)

lista.sort(reverse=True)

print ("O Maior número da Lista é o:",lista [0])
