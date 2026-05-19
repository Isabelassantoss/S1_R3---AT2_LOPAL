#Exercício 5
nome = input("Digite seu nome: ")
while len(nome) <= 3:
    print("Erro! O nome deve ter mais de 3 caracteres.")
    nome = input("Digite seu nome novamente: ")

idade = int(input("Digite sua idade: "))
while idade not in range(0, 151):
    print("Erro! A idade deve estar entre 0 e 150.")
    idade = int(input("Digite sua idade novamente: "))

salario = float(input("Digite seu salário: "))
while salario <= 0:
    print("Erro! Salário deve ser maior que zero.")
    salario = float(input("Digite novamente: "))


sexo = input("Sexo (f/m): ").lower()
while sexo not in "fm":
    print("Erro! Digite apenas 'f' ou 'm'.")
    sexo = input("Sexo (f/m): ").lower()

estado_civil = input("Estado Civil (s, c, v, d): ").lower()
opcoes = ['s', 'c', 'v', 'd']

while estado_civil not in opcoes:
    print(f"Erro! As opções aceitas são {opcoes}")
    estado_civil = input("Estado Civil (s, c, v, d): ").lower()

print("Dados validados com sucesso!")