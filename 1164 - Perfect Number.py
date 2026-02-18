N = int(input())
divisores = []

for _ in range(N):
    X = int(input())
    divisor = X//2
    while divisor != 0:
        if X % divisor == 0:
            divisores.append(divisor)
        divisor -= 1

    if sum(divisores) == X:
        print(f'{X} eh perfeito')
    else:
        print(f'{X} nao eh perfeito')
    divisores = []
