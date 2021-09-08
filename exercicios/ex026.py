frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('A posição que aparece pela primeira vez é {} e a última é {}'
      .format(frase.find('A')+1, frase.rfind('A')+1))
