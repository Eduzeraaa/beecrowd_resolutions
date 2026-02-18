N = int(input())
for _ in range(N):
    total = 0
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    if X > Y:
        Y += 1
        while X > Y:
            X -= 1
            if X % 2 == 1:
                total += X
        print(total)
        
    elif Y > X:
        X += 1
        while Y > X:
            Y -= 1
            if Y % 2 == 1:
                total += Y
        print(total)
        
    elif Y == X:
        print('0')
