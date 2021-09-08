from math import hypot
a = float(input('Qual é o comprimento do cateto oposto? '))
b = float(input('Qual é o comprimento do cateto adjacente? '))
print('A hipotenusa do triângulo retângulo é {:.2f}'.format(hypot(a, b)))

