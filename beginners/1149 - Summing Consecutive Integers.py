numeros = input().split()
numerosint = []
contador = 0
total = 0

while numeros != []:
    numero = numeros.pop(0)
    numero = int(numero)
    numerosint.append(numero)

A = numerosint.pop(0)

while True:
    N = numerosint.pop(0)
    if N <= 0:
        continue
    else:    
        break


for i in range(N):
    total += A + contador
    contador += 1
print(total)
