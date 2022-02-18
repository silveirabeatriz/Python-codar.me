#funcoes

#funcao com argumentos posicionais, posicao dos parametros importa

def dar_boas_vindas (nome,sobrenome,nome_do_curso):
    print ("Olá,", nome, sobrenome)
    print ("Bem-vindo ao curso de", nome_do_curso)
    
# dar_boas_vindas ("Gabriel","Saldanha","JavaScrip")

#kewyword arguments

dar_boas_vindas(nome="Gabriel", nome_do_curso="JavaScript", sobrenome="Saldanha")

#argumentos posicionais devem vir antes de argumentos nomeados

def calcular_conta(consumo, taxa_servico, desconto_fidelidade):
    #if taxa_servico == 0 and desconto_fidelidade == 0:
    #    return consumo
    
    servico = consumo * taxa_servico
    desconto = consumo * desconto_fidelidade
    valor = consumo + servico
    valor = valor - desconto
    return valor
    
valor = calcular_conta(consumo=100, taxa_servico=0.10, desconto_fidelidade=0.05)
print("O valor a ser pago é:", valor)

"""
consumo = 100
servico = consumo * taxa_servico #10
desconto = consumo * desconto_fidelidade # 5

valor = consumo + servico # 100+10 =110
valor = valor - desconto #110-5
-> 105
"""
