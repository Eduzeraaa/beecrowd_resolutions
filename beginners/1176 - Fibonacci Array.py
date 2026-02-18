N = int(input())
for _ in range(N):
    anterior = 0
    atual = 1
    novo = 0
    T = int(input())
    
    if T == 0:
        print(f'Fib(0) = 0')
    elif T == 1:
        print(f'Fib(1) = 1')
    elif T > 1:
        for _ in range(T - 1):
            novo = atual + anterior
            anterior = atual
            atual = novo

        print(f'Fib({T}) = {novo}')
