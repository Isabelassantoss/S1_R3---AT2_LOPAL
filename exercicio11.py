#Exercício 11
numero = int(input("Digite um número de 1 a 10 para ver a tabuada: "))
print("\n")
print("Tabuada {}\n".format(numero))
print("-" * 13)

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

print("-" * 13)