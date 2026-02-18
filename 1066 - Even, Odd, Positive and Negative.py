n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())

contadorpar = 0
contadorimpar = 0
contadorpos = 0
contadorneg = 0

for num in [n1, n2, n3, n4, n5]:
    if num % 2 == 0:
        contadorpar += 1
    
    if num % 2 == 1:
        contadorimpar += 1
    
    if num > 0:
        contadorpos += 1
    
    if num < 0:
        contadorneg += 1

print(f'''{contadorpar} valor(es) par(es)
{contadorimpar} valor(es) impar(es)
{contadorpos} valor(es) positivo(s)
{contadorneg} valor(es) negativo(s)''')
