# Define a senha correta
senha_correta = 2002

while True:
    #Verifica a senha digitada
    senha = int(input("Digite sua senha: "))

    # Verifica se a senha está correta
    if senha == senha_correta:
        print("Acesso Permitido")
        break
    else:
        print("Senha Inválida")