# 14) Escreva um programa para controlar uma pequena máquina registradora.
# Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
# Utilize a tabela de códigos abaixo para obter o preço de cada produto:
# Código    Preço
# 1         0,50
# 2         1,00
# 3         4,00
# 5         7,00
# 9         8,00
# Seu programa deve exibir o total das compras depois que o usuário digitar 0.
# Qualquer outro código deve gerar a mensagem de erro “Código inválido”.

cod = 1
total = 0
while cod != 0:
    cod = int(input('Digite o código do produto:'))
    if cod == 1:
        total = total + 0.5
    elif cod == 2:
        total = total + 1
    elif cod == 3:
        total = total + 4
    elif cod == 5:
        total = total + 7
    elif cod == 9:
        total = total + 8
    elif cod == 0:
        print('Calculando o valor a pagar...')
    else:
        print("Código inválido")

print(f'Total a pagar R${total}')