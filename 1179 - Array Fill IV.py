pares = []
impares = []
for _ in range (15):
    contadorpar = 0
    contadorimpar = 0
    N = int(input())
    match N % 2:
        case 0:
            pares.append(N)
        case _:
            impares.append(N)

    if len(pares) == 5:
        while pares != []:
            atual = pares.pop(0)
            print(f'par[{contadorpar}] = {atual}')
            contadorpar += 1

    if len(impares) == 5:
        while impares != []:
            atual = impares.pop(0)
            print(f'impar[{contadorimpar}] = {atual}')
            contadorimpar += 1

while impares != []:
            atual = impares.pop(0)
            print(f'impar[{contadorimpar}] = {atual}')
            contadorimpar += 1
while pares != []:
            atual = pares.pop(0)
            print(f'par[{contadorpar}] = {atual}')
            contadorpar += 1
