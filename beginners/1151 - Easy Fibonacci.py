N = int(input())
fib = 0
fib2 = 1

if N % 2 == 1:
    for _ in range(N//2):
        print(f'{fib} {fib2}', end=' ')
        N -= 1
        fib = fib+fib2
        fib2 = fib2+fib
    print(fib)

elif N % 2 == 0:
    for _ in range((N//2)-1):
        print(f'{fib} {fib2}', end=' ')
        N -= 1
        fib = fib+fib2
        fib2 = fib2+fib
    print(fib, fib2)
