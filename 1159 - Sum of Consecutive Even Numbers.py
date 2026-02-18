x = int(input())
pares = []

while x != 0:
    if x % 2 == 0:
        pares.append(x)
        for _ in range (4):
            x += 2
            pares.append(x)
        print(sum(pares))
        x = int(input())
        pares = []
    
    else:
        x += 1
        pares.append(x)
        for _ in range (4):
            x += 2
            pares.append(x)
        print(sum(pares))
        x = int(input())
        pares = []
