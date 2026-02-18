N = int(input())
contador = 0
numeros = []
dentro = 0
fora = 0
while contador != N:
    num = int(input())
    numeros.append(num)
    contador += 1

while numeros != []:
    number = numeros.pop(0)
    if 10 <= number <= 20:
        dentro += 1
    else:
        fora += 1

print(f'{dentro} in\n{fora} out')
