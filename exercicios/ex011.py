altura = float(input('Qual é a altura da parede que você quer pintar? '))
largura = float(input('Qual é a largura da parede que você quer pintar? '))
print('Você tem uma àrea de {:.2f} metros e precisa de {:.2f} litro(s) de tinta!'
      .format(altura*largura, (altura*largura)/2))
