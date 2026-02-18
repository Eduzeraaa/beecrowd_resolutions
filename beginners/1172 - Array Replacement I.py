lista = []
for indice in range(10):
    X = int(input())
    if X < 1:
        X = 1
    lista.append(X)
    print(f'X[{indice}] = {lista.pop(0)}')
    indice += 1
