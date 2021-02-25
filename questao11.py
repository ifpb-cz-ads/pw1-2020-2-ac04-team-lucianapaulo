#11) Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
#Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.

valor_inicial = float(input("Digite o valor inicial do primeiro deposito:"))
taxa_juros = float(input("Digite a taxa dejuros aos mês:"))
valor_no_mes = valor_inicial
deposito_mensal = 0
depositos_totais = 0
meses = 12
cont = 1
while cont <=12:
  if cont != 1:
    deposito_mensal = float(input('Digite o valor depositado nesse mês: '))
  valor_no_mes = valor_no_mes + deposito_mensal
  depositos_totais = depositos_totais + deposito_mensal
  valor_no_mes = valor_no_mes + valor_no_mes * (taxa_juros / 100)
  print(f'No final do mês {cont} você tinha {valor_no_mes}')
  cont = cont + 1
ganho = valor_no_mes - valor_inicial - depositos_totais
print(f'Total ganho com juros: {ganho}')