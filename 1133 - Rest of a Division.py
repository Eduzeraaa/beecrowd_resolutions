x = int(input())
y = int(input())

inicio = min(x, y)
fim = max(x, y)

for _ in range (inicio + 1, fim):
    if _ % 5 == 2 or _ % 5 == 3:
        if _ > 0:
            print(_)
