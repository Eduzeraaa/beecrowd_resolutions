lista = []
for _ in range(20):
    N = int(input())
    lista.append(N)

lista.reverse()
for indice in range(20):
    print(f'N[{indice}] = {lista.pop(0)}')
