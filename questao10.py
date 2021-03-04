#10) Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
#Exiba os valores mês a mês para os 12 primeiros meses. Escreva o total ganho com juros no período.

valor_inicial = float(input("Digite o valor do deposito:"))
taxa_juros = float(input("Digite a taxa dejuros aos mês:"))
valor_no_mes = valor_inicial
meses = 12
cont = 1
while cont <=12:
  valor_no_mes = valor_no_mes + valor_no_mes * (taxa_juros / 100)
  print(f'No final do mês {cont} você tinha {valor_no_mes}')
  cont = cont + 1
ganho = valor_no_mes - valor_inicial
print(f'Total ganho com juros: {ganho}')