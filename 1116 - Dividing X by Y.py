N = int(input())

for _ in range(N):
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    
    if Y != 0:
        print(f'{X/Y:.1f}')
        
    else:
        print('divisao impossivel')
