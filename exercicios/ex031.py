distancia = float(input('Qual a distância em Km da viagem que quer fazer? '))
if distancia <= 200:
    print('O preço da passagem é R$ {:.2f}'.format(distancia * 0.50))
else:
    print('O preço da passagem é R$ {:.2f}'.format(distancia * 0.45))