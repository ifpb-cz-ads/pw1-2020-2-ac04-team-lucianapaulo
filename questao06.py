# Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, 
# em vez de começar com 1 e 10.

tab = int(input("Tabuada do: "))
inicio = int(input('Informe de onde começa a tabuada: '))
fim = int(input('Informe onde termina a tabuada: '))

for i in range(inicio, fim+1):
  print(f'{tab} * {i} = {tab*i}')

