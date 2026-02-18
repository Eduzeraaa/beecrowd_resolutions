X, Y = input().split()
X = int(X)
Y = int(Y)

if X == 1:
    X = 4.00

elif X == 2:
    X = 4.50

elif X == 3:
    X = 5.00

elif X == 4:
    X = 2.00

elif X == 5:
    X = 1.50

print(f'Total: R$ {X * Y:.2f}')
