A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
reserva = None

lista = [A, B, C]
lista.sort()
lista.reverse()

A = lista.pop(0)
B = lista.pop(0)
C = lista.pop(0)

if A >= B + C:
        print('NAO FORMA TRIANGULO')
else:
    if A**2 == B**2 + C**2:
            print('TRIANGULO RETANGULO')

    if A**2 > B**2 + C**2:
            print('TRIANGULO OBTUSANGULO')

    if A**2 < B**2 + C**2:
            print('TRIANGULO ACUTANGULO')

    if A == B and B == C and A == C:
            print('TRIANGULO EQUILATERO')

    if A == B != C or A == C != B or B == C != A:
            print('TRIANGULO ISOSCELES')
