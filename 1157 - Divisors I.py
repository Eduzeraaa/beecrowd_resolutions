N = int(input())
denominador = N

while denominador != 0:
    if N % denominador == 0:
        print(f'{N/denominador:.0f}')
    denominador -= 1
