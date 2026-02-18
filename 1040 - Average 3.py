N1, N2, N3, N4 = input().split()

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

average = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10

if average > 7:
    print(f'Media: {average:.1f}\nAluno aprovado.')

elif 5 <= average < 6.9:
    print(f'Media: {average:.1f}')
    print('Aluno em exame.')
    N5 = float(input())
    new_average = (average + N5) / 2
    
    if new_average >= 5:
        print(f'Nota do exame: {N5}')
        print('Aluno aprovado.')
        print(f'Media final: {new_average:.1f}')
    
    else:
        print(f'Nota do exame: {N5}')
        print('Aluno reprovado.')
        print(f'Media final: {new_average:.1f}')

elif average < 5:
    print(f'Media: {average:.1f}\nAluno reprovado.')
