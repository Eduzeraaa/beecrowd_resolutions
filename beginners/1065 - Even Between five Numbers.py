n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())

contador = 0

for even in [n1, n2, n3, n4, n5]:
    if even % 2 == 0:
        contador += 1

print(f'{contador} valores pares')
