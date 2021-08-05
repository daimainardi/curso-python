# n1 = input('Digite um valor: ')
# print(type(n1))
# se deixar assim ele entende que é uma string
# n1 = int(input('Digite um valor: '))
# print(type(n1))
# converteu para numero inteiro

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
# print('A soma dos números', n1, 'e', n2,'é igual a', soma)
print('A soma dos números {} e {} é igual a {}'.format(n1, n2, soma))
