#from random import choice as sorteio
#num = random.randint(1, 10)
#print(num)
#print('O aluno sorteado para apagar o quadro hoje é: {}'
#      .format(sorteio(['Daiane', 'Daniel', 'Marcelo', 'Fernando'])))
from random import choice
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
print('O aluno sorteado para apagar o quadro é: {}'.format(choice([a1, a2, a3, a4])))

