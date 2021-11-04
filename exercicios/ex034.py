salario = float(input('Qual é o seu salário? R$ '))
if salario > 1250.00:
    novo_salario = salario + salario / 10
else:
    novo_salario = salario + salario / 100 * 15
print('Seu novo salário será R$: {:.2f}'.format(novo_salario))
