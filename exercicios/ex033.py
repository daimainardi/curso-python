#n1 = int(input('Digite o primeiro número: '))
#n2 = int(input('Digite o segundo número: '))
#n3 = int(input('Digite o terceiro número: '))
#if n1 == n2 or n1 == n3 or n2 == n3:
#    print('Digite números diferentes!')
#lista = [n1,n2,n3]
#print(f'O maior número é: {max(lista)}')
#print(f'O menor número é: {min(lista)}')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 == n2 or n1 == n3 or n2 == n3:
    print('Digite números diferentes!')
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
    print(f'O maior número é: {maior}')
    print(f'O menor número é: {menor}')
