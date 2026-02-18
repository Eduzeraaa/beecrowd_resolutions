alcool = 0
gasolina = 0
diesel = 0
while True:
    N = int(input())
    if N == 1:
        alcool += 1
    elif N == 2:
        gasolina += 1
    elif N == 3:
        diesel += 1
    elif N == 4:
        break
    else:
        continue

print(f'''MUITO OBRIGADO
Alcool: {alcool}
Gasolina: {gasolina}
Diesel: {diesel}''')
