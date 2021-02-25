#16) Escreva um programa que leia um número e verifique se é ou não um número primo.
#Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por
#todos os números ímpares até o número lido. Se o resto de uma dessas divisões for igual
#a zero, o número não é primo. Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.

numero = int(input('Digite um número:'))
divisores = 0
for i in range(1, numero+1):
  if numero % i == 0:
    divisores = divisores + 1
if divisores == 2:
  print(f'O número {numero} é primo')
else:
  print(f'O número {numero} não é primo')