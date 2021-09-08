n = int(input('Digite o número que deseja saber a tabuada: '))
print('A tabuada do número {} é:'.format(n))
print('=' * 12)
for m in range(0, 11):
    print('{} x {:2} = {}'.format(n, m, n*m))
print('=' * 12)


