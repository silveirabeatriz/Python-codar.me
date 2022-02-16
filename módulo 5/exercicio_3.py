USUARIO = "admin"
SENHA = "12345"

nome_usuario = input("Digite o nome de usuario:\n")
senha_usuario = input("Digite a sua senha: \n")

if (nome_usuario == USUARIO) and (senha_usuario == SENHA):
    print ( "Autenticacao bem Sucedida")
elif (nome_usuario != USUARIO) and (senha_usuario != SENHA):
    print("Usuario e Senha incorretos.")
elif (nome_usuario != USUARIO):
    print ("Usuario nao existe.")
elif (senha_usuario != USUARIO):
    print ("Senha incorreta.")
