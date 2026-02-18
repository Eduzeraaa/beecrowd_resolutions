from math import sqrt

A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

delta = (B)**2 - 4 * A * C

if delta < 0 or A == 0:
    print('Impossivel calcular')
else:
    R1 = ((-B) + sqrt(delta)) / (2 * A)
    R2 = ((-B) - sqrt(delta)) / (2 * A)
    print(f'R1 = {R1:.5f}\nR2 = {R2:.5f}')
