# Exercício 6
num = int(input("Digite um número inteiro: "))
if num < 2:
  print("Esse número não é primo".format(num))
else:
  for i in range (2, num):
    if num % i == 0:
      print("Esse numero não é primo". format(num))
      break
  else:
    print("Esse número primo!". format(num))