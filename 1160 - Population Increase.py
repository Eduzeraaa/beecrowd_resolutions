T = int(input())

for _ in range(T):
    PA, PB, G1, G2 = input().split()
    PA = int(PA)
    PB = int(PB)
    G1 = float(G1)
    G2 = float(G2)
    anos = 0
    
    while PA <= PB:
        if G2 == 0:
            PA = PA + (PA*(G1/100))
            PA = int(PA)
            anos += 1
            if anos > 100:
                break
        else:
            PA = PA + (PA*(G1/100))
            PB = PB + (PB*(G2/100))
            PA = int(PA)
            PB = int(PB)
            anos += 1
            if anos > 100:
                break
    if anos > 100:
        print('Mais de 1 seculo.')
    else:
        print(f'{anos} anos.')
