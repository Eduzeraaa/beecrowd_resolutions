salary = float(input())

if 0 < salary <= 400:
    percent = 0.15
    augment = salary * percent
    new_salary = salary + augment
    print(f'Novo salario: {new_salary:.2f}\nReajuste ganho: {augment:.2f}\nEm percentual: {percent*100:.0f} %')
elif 400.01 <= salary <= 800:
    percent = 0.12
    augment = salary * percent
    new_salary = salary + augment
    print(f'Novo salario: {new_salary:.2f}\nReajuste ganho: {augment:.2f}\nEm percentual: {percent*100:.0f} %')
elif 800.01 <= salary <= 1200:
    percent = 0.1
    augment = salary * percent
    new_salary = salary + augment
    print(f'Novo salario: {new_salary:.2f}\nReajuste ganho: {augment:.2f}\nEm percentual: {percent*100:.0f} %')
elif 1200.01 <= salary <= 2000:
    percent = 0.07
    augment = salary * percent
    new_salary = salary + augment
    print(f'Novo salario: {new_salary:.2f}\nReajuste ganho: {augment:.2f}\nEm percentual: {percent*100:.0f} %')
elif salary > 2000:
    percent = 0.04
    augment = salary * percent
    new_salary = salary + augment
    print(f'Novo salario: {new_salary:.2f}\nReajuste ganho: {augment:.2f}\nEm percentual: {percent*100:.0f} %'
