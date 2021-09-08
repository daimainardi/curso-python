from math import sqrt

# n = int(input('Digite um número: '))
# print('Você digitou o número {}\nO dobro é {}\nO triplo é {}\nA raiz quadrada é {:.3f}'
#       .format(n, n*2, n*3, n**(1/2), n**3))

n = int(input('Digite um número: '))
print('Você digitou o número {}\nO dobro é {}\nO triplo é {}\nA raiz quadrada é {:.3f}\nElevado na terceira fica {}'
      .format(n, n*2, n*3, sqrt(n), pow(n,3)))
