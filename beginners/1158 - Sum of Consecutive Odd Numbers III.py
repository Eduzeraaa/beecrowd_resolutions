N = int(input())
impares = []

for _ in range(N):
    x, y = input().split()
    x = int(x)
    y = int(y)
    
    if x % 2 != 1:
        x += 1
            
    for i in range(y):
        impares.append(x)
        x += 2
    print(sum(impares))
    impares = []
