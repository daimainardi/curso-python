velocidade = float(input('Qual a velocidade do carro em km\h? '))
if velocidade > 80:
    print('Você foi multado! O valor da multa será de R${:.2f}'.format((velocidade - 80)*7))
else:
    print('Dirija com segurança, boa viagem!!!')
