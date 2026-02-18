n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())
contador = 0
for positive in [n1, n2, n3, n4, n5, n6]:
    if positive > 0:
        contador += 1
print(f'{contador} valores positivos')
