from math import sin, cos, tan, radians
angulo = float(input('Me fale um ângulo qualquer: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O seno é {:.2f}\nO cosseno é {:.2f}\nA tangente é {:.2f}'
      .format(seno, cosseno, tangente))