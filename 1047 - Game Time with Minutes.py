hr1, min1, hr2, min2 = input().split()
hr1 = int(hr1)
min1 = int(min1)
hr2 = int(hr2)
min2 = int(min2)

if hr2 < hr1:
    hr2 += 24

minutos_iniciais = (hr1 * 60) + min1
minutos_finais = (hr2 * 60) + min2
soma = minutos_finais - minutos_iniciais

horas = soma // 60
minutos = soma % 60

if horas == 0 and minutos == 0:
    horas = 24
    minutos = 0

elif soma < 60:
    horas = 0
    minutos = soma

if minutos < 0:
    soma = minutos_finais - minutos_iniciais + 1440
    horas = soma // 60
    minutos = soma % 60

    if horas == 0 and minutos == 0:
        horas = 24
        minutos = 0

    elif soma < 60:
        horas = 0
        minutos = soma
print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
