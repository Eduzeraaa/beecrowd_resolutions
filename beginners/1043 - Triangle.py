A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

if A < B + C and B < A + C and C < A + B:
    print(f'Perimetro = {A+B+C:.1f}')

else:
    print(f'Area = {((A + B) / 2) * C}')
