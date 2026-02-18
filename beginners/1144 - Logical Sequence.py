N = int(input())
p, s, t = 0, 0, 0
for i in range(N):
    p += 1
    s = p ** 2
    t = p ** 3
    print(f'{p} {s} {t}')
    print(f'{p} {s + 1} {t + 1}')
