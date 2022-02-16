num = int (input ("Digite um numero inteiro: \n"))
i = 1
aux = 0

while i <= num:
    if num%i==0:
        aux += 1
    i += 1

if aux == 2:
    print ("O numero é Primo")
else:
    print ("O numero nao é Primo")