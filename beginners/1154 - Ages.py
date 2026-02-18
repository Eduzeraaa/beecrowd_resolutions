N = int(input())
numeros = []
quant = 0

while N >= 0:
    quant += 1
    numeros.append(N)
    N = int(input())

total = sum(numeros)
media = total/quant
print(f'{media:.2f}')
