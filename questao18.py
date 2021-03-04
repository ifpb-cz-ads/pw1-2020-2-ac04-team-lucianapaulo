#18) Escreva um programa que calcule o resto da divisão inteira entre dois números.
#Utilize apenas as operações de soma e subtração para calcular o resultado.

a = int(input("Digite um número:"))
b = int(input("Digite outro número:"))
resto = a
if a>=b:
  while resto >= b:
    resto = resto - b
print(f'Resto {resto}')