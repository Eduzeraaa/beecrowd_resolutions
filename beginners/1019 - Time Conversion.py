N = int(input())

hrs = N // 3600
minrestantes = N - (hrs * 3600)

minutos = minrestantes // 60

segrestantes = minrestantes - ( minutos * 60)

print(f'{hrs}:{minutos}:{segrestantes}')
