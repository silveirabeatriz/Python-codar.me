numero = int (input("Para encerrar o programa digite um numero inteiro negativo.\nDigite um número inteiro positivo:\n"))

lista = []

while numero >= 0:
    lista.append(numero)
    numero = int (input("Digite um número inteiro positivo:\n"))
print (lista)