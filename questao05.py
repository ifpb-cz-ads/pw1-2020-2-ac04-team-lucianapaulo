# 5) Altere o programa abaixo para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2=4, ...
tab = int(input("Tabuada do: "))

for i in range(1, 11):
  print(f'{tab} * {i} = {tab*i}')
