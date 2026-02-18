code1, units1, value1 = input().split()
code2, units2, value2 = input().split()

units1 = int(units1)
value1 = float(value1)

units2 = int(units2)
value2 = float(value2)

total = (units1 * value1) + (units2 * value2)

print(f"VALOR A PAGAR: R$ {total:.2f}")
