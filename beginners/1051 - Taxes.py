N = float(input())
total1 = 0
total2 = 0


if 0 < N <= 2000:
    print('Isento')

elif 2000.01 <= N <= 3000:
    N -= 2000
    total = N * 0.08
    print(f'R$ {total:.2f}')

elif 3000.01 <= N <= 4500:
    total1 = N - 3000
    taxa = total1 * 0.18
    N = N - total1 - 2000
    total = N * 0.08
    print(f'R$ {total+taxa:.2f}')

elif N > 4500:
    total2 = N - 4500
    total1 = N - total2 - 3000
    
    taxa1 = total1 * 0.18
    taxa2 = total2 * 0.28
    N = N - total2 - total1 - 2000
    total = N * 0.08
    print(f'R$ {total+taxa1+taxa2:.2f}')
