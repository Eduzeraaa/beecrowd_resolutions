L = int(input())
T = input()

matriz = []
for duzia in range(12):
    linha = []
    for coluna in range(12):
        number = float(input())
        linha.append(number)
    matriz.append(linha)

coluna_selecionada = [matriz[i][L] for i in range(12)]

if T == 'S':
    print(f'{sum(coluna_selecionada):.1f}')
elif T == 'M':
    print(f'{sum(coluna_selecionada)/12:.1f}')
