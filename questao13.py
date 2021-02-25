#13) Escreva um programa que leia números inteiros do teclado.
#O programa deve ler os números até que o usuário digite 0 (zero).
#No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

numero = 1
soma = 0
quant = 0

while numero != 0:
  numero = int(input('Digite um número:'))
  quant = quant + 1
  soma = soma + numero
media = soma / quant
print(f'Quantidade de numeros digitados: {quant}')
print(f'Soma: {soma}')
print(f'Média aritmética: {media}')