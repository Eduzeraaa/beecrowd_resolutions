N = int(input())

while N != 0:
    num = int(input())
    if num > 0 and num % 2 == 0:
        print('EVEN POSITIVE')
    
    elif num > 0 and num % 2 == 1:
        print('ODD POSITIVE')

    elif num < 0 and num % 2 == 0:
        print('EVEN NEGATIVE')

    elif num < 0 and num % 2 == 1:
        print('ODD NEGATIVE')

    else:
        print('NULL')

    N -= 1
