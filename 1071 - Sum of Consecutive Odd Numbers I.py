x = int(input())
y = int(input())

total = 0

while x != y:
    if x > y:
        x -= 1
        if x == y:
            break
        if x % 2 == 1:
            total += x
        

    if y > x:
        y -= 1
        if x == y:
            break
        if y % 2 == 1:
            total += y
        


print(total)
