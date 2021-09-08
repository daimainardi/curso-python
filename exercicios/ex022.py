nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome com letras maiúsculas é {}\nSeu nome com letras minúsculas é {}'
      .format(nome.upper(), nome.lower()))
print('Seu nome completo tem {} letras\nSeu primeiro nome tem {} letras'
      .format(len(''.join(nome.split())), len(nome.split()[0])))