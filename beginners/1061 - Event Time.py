comeco = input()
horariocomeco = input()
fim = input()
horariofim = input()

separacaocomeco = comeco.split()
diacomeco = separacaocomeco.pop(1)
diacomeco = int(diacomeco)

separacaofim = fim.split()
diafim = separacaofim.pop(1)
diafim = int(diafim)

separacaohrcomeco = horariocomeco.split()
hrcomeco = separacaohrcomeco.pop(0)
hrcomeco = int(hrcomeco)
mincomeco = separacaohrcomeco.pop(1)
mincomeco = int(mincomeco)
segcomeco = separacaohrcomeco.pop(2)
segcomeco = int(segcomeco)
dia1total = (diacomeco * 86400) + (hrcomeco * 3600) + (mincomeco * 60) + segcomeco



separacaohrfim = horariofim.split()
hrfim = separacaohrfim.pop(0)
hrfim = int(hrfim)
minfim = separacaohrfim.pop(1)
minfim = int(minfim)
segfim = separacaohrfim.pop(2)
segfim = int(segfim)
dia2total = (diafim * 86400) + (hrfim * 3600) + (minfim * 60) + segfim


duracao = dia2total - dia1total

diastotais = duracao // 86400
horastotais = (duracao - (diastotais * 86400)) // 3600
mintotais = (duracao - (diastotais * 86400) - (horastotais * 3600)) // 60
segtotais = (duracao - (diastotais * 86400) - (horastotais * 3600) - (mintotais * 60)) % 60

print(f'''{diastotais} dia(s)
{horastotais} hora(s)
{mintotais} minuto(s)
{segtotais:.0f} segundo(s)''')
