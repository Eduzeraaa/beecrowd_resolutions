name = input('')
fix_salary = float(input(""))
products_sold = float(input(""))

total = fix_salary + (products_sold * 0.15)

print(f'TOTAL = R$ {total:.2f}')
