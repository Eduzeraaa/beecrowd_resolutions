A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

if A > B and A > C and B > C:
    print(f'''{C}\n{B}\n{A}\n\n{A}\n{B}\n{C}''')

elif A > B and A > C and C > B:
    print(f'{B}\n{C}\n{A}\n\n{A}\n{B}\n{C}')

elif B > A and B > C and A > C:
    print(f'{C}\n{A}\n{B}\n\n{A}\n{B}\n{C}')

elif B > A and B > C and C > A:
    print(f'{A}\n{C}\n{B}\n\n{A}\n{B}\n{C}')

elif C > A and C > B and B > A:
    print(f'{A}\n{B}\n{C}\n\n{A}\n{B}\n{C}')

elif C > A and C > B and A > B:
    print(f'{B}\n{A}\n{C}\n\n{A}\n{B}\n{C}')
