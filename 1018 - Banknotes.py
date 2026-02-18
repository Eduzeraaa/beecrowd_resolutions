N = int(input())

nota100 = N // 100
resto100 = N - (nota100 * 100)


nota50 = resto100 // 50
resto50 = resto100 - (nota50 * 50)


nota20 = resto50 // 20
resto20 = resto50 - (nota20 * 20)


nota10 = resto20 // 10
resto10 = resto20 - (nota10 * 10)


nota5 = resto10 // 5
resto5= resto10 - (nota5 * 5)


nota2 = resto5 // 2
resto2 = resto5 - (nota2 * 2)


nota1 = resto2 // 1
resto1 = resto2 - (nota1 * 1)


print(f'''{N}
{nota100} nota(s) de R$ 100,00
{nota50} nota(s) de R$ 50,00
{nota20} nota(s) de R$ 20,00
{nota10} nota(s) de R$ 10,00
{nota5} nota(s) de R$ 5,00
{nota2} nota(s) de R$ 2,00
{nota1} nota(s) de R$ 1,00''')
