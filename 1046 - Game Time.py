A, B = input().split()
A = int(A)
B = int(B)

lista = [A, B]

primeiro = lista.pop(0)
horario_inicial = 24 - primeiro
segundo = lista.pop(0)
total = horario_inicial + segundo
if total > 24:
    total -= 24
print(F'O JOGO DUROU {total} HORA(S)')
