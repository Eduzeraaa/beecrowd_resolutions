N = int(input())
divisores = 0

while divisores != 10000:
    if divisores % N == 2:
        print(divisores)
    divisores += 1
