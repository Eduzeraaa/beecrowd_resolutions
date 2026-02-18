N = int(input())

ano = N // 365
restoano = N % 365

mes = restoano // 30

dia = N - (ano * 365 + mes * 30)


print(f'''{ano} ano(s)
{mes} mes(es)
{dia} dia(s)''')
