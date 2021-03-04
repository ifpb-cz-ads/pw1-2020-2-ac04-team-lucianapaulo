#15) Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair.
#Imprima a tabuada da operação escolhida. Repita até que a opção "saída" seja escolhida.

opcao = 1

while opcao != 0:
  opcao = int(input('Digite 1 para a tabuada da adição, 2 para a de sutração \n 3 para a de multiplicação, 4 para a de divisão e 0 para sair:'))
  if opcao == 1:
    n = int(input("Tabuada de: "))
    x = 1
    while x <= 10:
      print(f'{n} + {x} = {n+x}')
      x=x+1
  elif opcao == 2:
    n = int(input("Tabuada de: "))
    x = 1
    while x <= 10:
      print(f'{n} - {x} = {n-x}')
      x=x+1
  elif opcao == 3:
    n = int(input("Tabuada de: "))
    x = 1
    while x <= 10:
      print(f'{n} x {x} = {n*x}')
      x=x+1
  elif opcao == 4:
    n = int(input("Tabuada de: "))
    x = 1
    while x <= 10:
      print(f'{n} / {x} = {n/x}')
      x=x+1
  elif opcao == 0:
    print('Até mais :)')
  else:
    print('Opção inválida')
