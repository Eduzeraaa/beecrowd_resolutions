lista = []
M, N = input().split()
M = int(M)
N = int(N)

while M > 0 and N > 0:
    
    if M > N:
        while M > N - 1:
            lista.append(M)
            M -= 1
            soma = sum(lista)
        lista.reverse()
        print(*lista, f'Sum={soma}')
    
    elif N > M:
        while N > M - 1:
            lista.append(N)
            N -= 1
            soma = sum(lista)
        lista.reverse()
        print(*lista, f'Sum={soma}')
    lista = []
    M, N = input().split()
    M = int(M)
    N = int(N)
