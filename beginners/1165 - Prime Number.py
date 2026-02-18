N = int(input())
divisores = []

for _ in range(N):
    X = int(input())
    divisor = X
    while divisor > 0:
        if X % divisor == 0:
            divisores.append(divisor)
            divisor -= 1

        else:
            divisor -= 1

    if len(divisores) == 2:
        print(f'{X} eh primo')
        
    else:
        print(f'{X} nao eh primo')
    divisores = []
