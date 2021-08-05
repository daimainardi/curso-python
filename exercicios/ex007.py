p1 = float(input('Qual nota você tirou na primeira prova? '))
p2 = float(input('Qual nota você tirou na segunda prova? '))
m = (p1+p2)/2
resultado = ''
if m >= 7:
    resultado = 'Aprovado'
elif 4 <= m < 7:
    resultado = 'Recuperação'
else:
    resultado = 'Reprovado'
print('Como as suas notas foram {} e {}, sua média final ficou {:.1f}\nResultado: {}'.format(p1, p2, m, resultado))

