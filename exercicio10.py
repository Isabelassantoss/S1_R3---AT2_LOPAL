#Exercicio 10
senha_correta = "676767"

tentativa = input("Digite sua senha: ")
while tentativa != senha_correta:
    print("Senha incorreta! Tente novamente.")
    tentativa = input("Digite sua senha: ")
print("Acesso liberado!")