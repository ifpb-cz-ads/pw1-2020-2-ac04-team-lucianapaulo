# Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro 
# pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se 
# de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. 
# Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))
total = 0

for i in range(int(n1)):
  total += n2

print(total)