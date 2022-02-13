valor_compras = float(input ("Digite o valor das compras:\n"))
desconto = float(input ("Digite o valor do desconto:\n"))
quantidade_itens= int(input("Digite a quantidade de itens:\n"))

valordesconto=valor_compras*desconto/100
valorfinal=valor_compras-valordesconto

custo_medio=valorfinal/quantidade_itens

print("O valor final de suas compras com o desconto aplicado é: ", valorfinal, "R$")
print("O custo médio de cada item é ", custo_medio, "R$")