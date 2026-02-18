numeros = []
for i in range (1, 101):
    decimal = 1/i
    numeros.append(decimal)

total = sum(numeros)
print(f'{total:.2f}')
