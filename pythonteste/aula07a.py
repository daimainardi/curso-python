# nome = input('Qual é o seu nome? ')
# print('Prazer em te conhecer {:20}!'.format(nome))
# print('Prazer em te conhecer {:>20}!'.format(nome))
# print('Prazer em te conhecer {:<20}!'.format(nome))
# print('Prazer em te conhecer {:^20}!'.format(nome))
# noinspection PyStringFormat
# print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Me dê um número: '))
n2 = int(input('Me dê outro número: '))
s = n1 + n2
m = n1 * n2
if n2 != 0:
    d = n1 / n2
    di = n1 // n2
else:
    d = 0
    di = 0
p = n1 ** n2
# print('A soma vale {}, o produto vale {}, a divisão vale {:.3f}, a divisão inteira vale {} e a potência vale {}'. format(s, m, d, di, p))
# print('A soma vale {}, o produto vale {} e a divisão vale {:.2f}'.format(s, m, d), end='. ')
# print('A divisão inteira vale {} e a potência vale {}'.format(di, p))
print('A soma vale {}\nO produto vale {}\nA divisão vale {:.2f}\nA divisão inteira vale {}\nA potência vale {}'
      .format(s, m, d, di, p))








