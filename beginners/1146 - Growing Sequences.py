while True:
    x = int(input())
    if x == 0:
        break
    else:
        for i in range (0, x -1):
            print(i + 1, end=' ')
    print(x)
