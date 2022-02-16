a = float(input ("Digite o 1° Operador:\n"))
b = float(input ("Digite o 2° Operador:\n"))

op = input("Digite o operador para o cálculo (+,-,*,/):\n")

resultado = 0


if op == "+":
    resultado = a+b
elif op == "-":
    resultado = a-b
elif op =="*":
    resultado = a*b
elif op =="/":
    if b!=0:
        resultado = a/b
    else:
        print ("Nao é possível realizar divisao por zero.")
print (resultado)

