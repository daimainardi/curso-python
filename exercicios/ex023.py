num = int(input('Digite um número de 1 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Este número é formado por:\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'
      .format(u, d, c, m))

