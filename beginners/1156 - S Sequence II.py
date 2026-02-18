numerador = 3
denominador = 2
parcial = 1

while numerador < 39:
    parcial = (numerador / denominador) + parcial
    numerador += 2
    denominador *= 2


print(f'{parcial:.2f}')
