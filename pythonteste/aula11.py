# \033 [0;30;41m
# \033 [4;33;44m
# \033[m para ficar padrão fundo preto e letra branca
# \033[7;30m para inverter o fundo para branco e letra preta
print('\033[4;30;45mOlá, Mundo!\033[m')
print('\033[7;30mSou uma vencedora!!!\033[m')
a = 4
b = 8
print('Os valores são \033[1;31m{}\033[m e \033[1;32m{}\033[m!!!'.format(a, b))
nome = 'Daniel'
print('O nome do meu marido é {}{}{}!!!'.format('\033[4;36m', nome, '\033[m'))