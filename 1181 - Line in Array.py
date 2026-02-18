L = int(input())
T = input()


matriz = []
for duzia in range(12):
    linha = []
    for coluna in range(12):
        number = float(input())
        linha.append(number)
    matriz.append(linha)
        
linha_selecionada = matriz[L]

if T == 'S':
    print(f'{sum(linha_selecionada):.1f}')

elif T == 'M':
    print(f'{sum(linha_selecionada)/12:.1f}')
