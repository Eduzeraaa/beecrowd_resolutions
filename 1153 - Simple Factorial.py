N = int(input())
fatorial = N

while N != 1:
    fatorial *= N - 1
    N -= 1

print(fatorial)
