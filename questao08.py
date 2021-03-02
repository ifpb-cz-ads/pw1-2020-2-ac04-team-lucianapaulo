'''
 Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, 
 assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado. 
 Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que 
 podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.

'''
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

if n1 == n2:
  print('A divisão inteira é: 1 E o resto da divisão é 0.')
else:
  count = 0

  while n1 > 0:
    n1 -= n2
    count += 1
  
    if n1 < n2:
      break
      
  print(f'A divisão inteira é: {count} E o resto da divisão é {n1}.')
  
