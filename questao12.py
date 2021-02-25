#12) Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal.
#Pergunte também o valor mensal que será pago.
#Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.

valor_inicial_divida = float(input('Digite o valor inicial da divida:'))
juros_mensais = float(input('Digite o valor do juros que está pagando:'))
valor_pago_no_mes = float(input('Digite o valor que pagará por mês:'))
divida = valor_inicial_divida
meses_para_quitar = 1
while divida >= 0:
  divida = divida + (divida * (juros_mensais / 100))
  divida = divida - valor_pago_no_mes
  meses_para_quitar = meses_para_quitar + 1
total_pago = meses_para_quitar * valor_pago_no_mes
total_juros_pago = total_pago - valor_inicial_divida
print(f'Número de meses para que a divida seja paga: {meses_para_quitar}')
print(f'Total pago: {total_pago}')
print(f'Total de juros pago: {total_juros_pago}')