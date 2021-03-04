#17) Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.

numero = int(input('Digite um número:'))
divisores = 0
aux = 0
primo = 1
while primo <= numero:
  for i in range(1, aux+1):
      if aux % i == 0:
        divisores = divisores + 1
  if divisores == 2:
    print(f'O número {aux} é primo')
    primo = primo + 1
  divisores = 0
  aux = aux + 1