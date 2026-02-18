N = float(input())
N *= 100

nota100 = N // 10000
resto100 = N % 10000
nota50 = resto100 // 5000
resto50 = resto100 % 5000
nota20 = resto50 // 2000
resto20 = resto50 % 2000
nota10 = resto20 // 1000
resto10 = resto20 % 1000
nota5 = resto10 // 500
resto5= resto10 % 500
nota2 = resto5 // 200
resto2 = resto5 % 200



moeda1 = resto2 // 100
restomoeda1 = resto2 % 100
cents50 = restomoeda1 // 50
resto50cents = restomoeda1 % 50
cents25 = resto50cents // 25
resto25cents = resto50cents % 25
cents10 = resto25cents // 10
restocents10 = resto25cents % 10
cents5 = restocents10 // 5
resto5cents = restocents10 % 5
cent = resto5cents // 1



print(f'''NOTAS:
{nota100:.0f} nota(s) de R$ 100.00
{nota50:.0f} nota(s) de R$ 50.00
{nota20:.0f} nota(s) de R$ 20.00
{nota10:.0f} nota(s) de R$ 10.00
{nota5:.0f} nota(s) de R$ 5.00
{nota2:.0f} nota(s) de R$ 2.00
MOEDAS:
{moeda1:.0f} moeda(s) de R$ 1.00
{cents50:.0f} moeda(s) de R$ 0.50
{cents25:.0f} moeda(s) de R$ 0.25
{cents10:.0f} moeda(s) de R$ 0.10
{cents5:.0f} moeda(s) de R$ 0.05
{cent:.0f} moeda(s) de R$ 0.01''')
