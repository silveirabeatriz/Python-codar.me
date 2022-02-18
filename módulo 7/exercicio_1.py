def e_primo(num):
    primo = True
    for n in range (2,int(num**0.5)+1):
        if num % n == 0:
            primo = False
    return primo

num = int(input("Digite um numero inteiro positivo, para saber se ele é Primo:\n"))

print (e_primo(num))

