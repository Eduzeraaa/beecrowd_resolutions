n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())

positivos = []
contador = 0
total = 0

for positive in [n1, n2, n3, n4, n5, n6]:
    if positive > 0:
        positivos.append(positive)
        contador += 1

while positivos != []:
    num = positivos.pop(0)
    total += num

media = total / contador
print(f'{contador} valores positivos\n{media:.1f}')
