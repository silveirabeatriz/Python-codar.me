print ("---------------ACERTE O NÚMERO---------------")
print ("Você tem 3 chances de acertar o número secreto.")
numero_secreto = 8
acertou = False
tentativas = 0

while (not acertou):
    if (tentativas >=3):
        print ("Você Perdeu! :(")
        break

    chute = int (input("Digite um numero inteiro:"))

    if chute == numero_secreto:
        print ("**ACERTOU! PARABÉNS!**")
        acertou = True    
    else:
        print ("Número errado!")

        if chute > numero_secreto:
            print ("Ainda nao acertou, o numero é menor.")
        elif chute < numero_secreto:
            print ("O numero secreto é maior.")

        tentativas +=1
