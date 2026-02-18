for i in range(0, 11):
    for j in range(1, 4):
        I = i / 5
        J = j + I

        if I.is_integer():
            I = int(I)
        if J.is_integer():
            J = int(J)

        print(f'I={I} J={J}')
