def maior_idade(pessoa):
    if pessoa[1] >= 18:
        maior = True
    elif pessoa [1] <=18:
        maior = False
    return maior

pessoa = ("Beatriz", 31)
nome, idade = pessoa

print("A pessoa é maior de idade?", maior_idade(pessoa))