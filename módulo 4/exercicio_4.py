valor_compra = float(input("Digite o valor da Compra:\n"))
valor_frete = float(input("Digite o valor do frete:\n"))
programa_fidelidade = input("Cadastrado no Programa de Fidelidade?[S ou N]\n")

valor_total = valor_compra + valor_frete

if valor_total>=100 or  programa_fidelidade =="S": 
    print ("Cupom de Desconto Liberado")
else:
    print ("Cupom de Desconto Negado")


