distancia = int(input('Qual a distância da sua viagem ? '))
if distancia <= 200:
    passagem = distancia * 0.50
    print('O valor da sua passagem é {} R$'.format(passagem))
else:
    passagem = distancia * 0.45
    print('O valor da sua passagem é {} R$'.format(passagem))