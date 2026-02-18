vitgremio = 0
vitinter = 0
empate = 0
grenais = 0
while True:
    inter, gremio = input().split()
    gremio = int(gremio)
    inter = int(inter)
    
    if gremio > inter:
        vitgremio += 1
    
    elif inter > gremio:
        vitinter += 1
    
    else:
        empate += 1
    
    grenais += 1
    print('Novo grenal (1-sim 2-nao)')
    escolha = int(input())
    while escolha != 1 and escolha != 2:
        print('Novo grenal (1-sim 2-nao)')
    
    if escolha == 2:
        break
print(f'''{grenais} grenais
Inter:{vitinter}
Gremio:{vitgremio}
Empates:{empate}''')
        
if vitgremio > vitinter:
        print('Gremio venceu mais')
        
elif vitinter > vitgremio:
        print('Inter venceu mais')
        
else:
        print('Não houve vencedor')
