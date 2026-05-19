#Exercício 2
numeros = []

for i in range(3):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

print("Maior número:", max(numeros))
print("Menor número:", min(numeros))