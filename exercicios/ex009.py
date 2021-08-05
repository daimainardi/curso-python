n = int(input('Digite o número que deseja saber a tabuada: '))
print('A tabuada do número {} é:'.format(n))
for m in range(0, 10):
    print('{} x {} = {}'.format(n, m, n*m))
