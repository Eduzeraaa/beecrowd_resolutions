T = int(input())
contador = 0
for indice in range(1000):
    print(f'N[{indice}] = {contador}')
    contador += 1
    if contador == T:
        contador = 0
