r1 = int(input('Qual é o comprimento da primeira reta: '))
r2 = int(input('Qual é o comprimento da segunda reta: '))
r3 = int(input('Qual é o comprimento da terceira reta: '))
lista = [r1, r2, r3]
if ((r1 + r2) > r3 and r3==max(lista)) or ((r1 + r3) > r2 and r2==max(lista)) or ((r2 + r3) > r1 and r1==max(lista)):
    print('Suas retas formam um triângulo!')
else:
    print('Suas retas não formam um triângulo!')
