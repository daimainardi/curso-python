from math import sqrt

# n = int(input('Digite um número: '))
# print('Você digitou o número {}\nO dobro é {}\no triplo é {}\na raiz quadrada é {:.3f}'
#       .format(n, n*2, n*3, n**(1/2)))

n = int(input('Digite um número: '))
print('Você digitou o número {}\nO dobro é {}\no triplo é {}\na raiz quadrada é {:.3f}\nelevado na terceira fica {}'
      .format(n, n*2, n*3, sqrt(n), pow(n,3)))
