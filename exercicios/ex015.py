km = float(input('Quantos km você percorreu de carro? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
print('O valor a pagar pelo aluguel do carro é R${:.2f}'.format(dias * 60 + 0.15 * km))

