velocidade = int(input('Informe a velocidade do carro: '))
limite = 80

if velocidade > limite:
    excesso = velocidade - limite
    multa = excesso * 7
    print('Você estava a cima da velocidade permitida e foi multado! O valor da multa é R$ {:.2f}'.format(multa))
else:
    print('Velocidade permitida,boa viagem!')
