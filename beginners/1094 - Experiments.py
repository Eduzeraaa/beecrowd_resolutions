N = int(input())
somaquantidade = 0
quantidadecoelho = 0 
quantidadesapo = 0
quantidaderato = 0

for animal in range (N):
    animal = input().upper()
    separacao = animal.split()
    tipo = separacao.pop(1)
    quantidade = separacao.pop(0)
    quantidade = int(quantidade)

    if tipo == 'C':
        quantidadecoelho += quantidade
    
    elif tipo == 'S':
        quantidadesapo += quantidade
    
    elif tipo == 'R':
        quantidaderato += quantidade

    quantidadetotal = quantidaderato + quantidadecoelho + quantidadesapo

    pctcoelho = (quantidadecoelho / quantidadetotal) * 100
    pctsapo = (quantidadesapo / quantidadetotal) * 100
    pctcorato = (quantidaderato / quantidadetotal) * 100

print(f'''Total: {quantidadetotal} cobaias
Total de coelhos: {quantidadecoelho}
Total de ratos: {quantidaderato}
Total de sapos: {quantidadesapo}
Percentual de coelhos: {pctcoelho:.2f} %
Percentual de ratos: {pctcorato:.2f} %
Percentual de sapos: {pctsapo:.2f} %''')
