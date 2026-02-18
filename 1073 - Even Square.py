N = int(input())
contador = 0

while contador != N:
    contador += 1
    if contador % 2 == 0:
        print(f'{contador}^2 = {contador**2}')
