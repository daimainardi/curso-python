from random import randint
sorteio = randint(0, 5)
entrada = input('Tente acertar um número de 0 a 5 que o computador sorteou: ')
num = 0
try:
    num = int(entrada)
except ValueError:
    print('Digite somente números')
    entrada = input('Tente acertar um número de 0 a 5 que o computador sorteou: ')
if num == sorteio:
    print('você venceu!!!')
else:
    print(f'Você perdeu, o computador sorteou {sorteio}!!!')
