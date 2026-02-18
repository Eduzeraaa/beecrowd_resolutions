sete = 5
quatro = 2
for i in range(-1, 9, 2):
    sete += 2
    quatro += 2
    for j in range(sete, quatro, -1):
        print(f'I={i+2} J={j}')
