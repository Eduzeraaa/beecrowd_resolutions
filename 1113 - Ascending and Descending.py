X, Y = input().split()
X = int(X)
Y = int(Y)

while X != Y:
    if X > Y:
        print('Decrescente')
        X, Y = input().split()
        X = int(X)
        Y = int(Y)
    elif Y > X:
        print('Crescente')
        X, Y = input().split()
        X = int(X)
        Y = int(Y)
