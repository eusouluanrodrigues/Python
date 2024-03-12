l1 = float(input('Informe o primeiro lado: '))
l2 = float(input('Informe o segundo lado: '))
l3 = float(input('Informe o terceiro lado: '))
if (l1 + l2 > l3) and (l1 +l3 > l2) and (l3 + l2 > l1 ):
    print('Forma triângulo')
else:
    print('Não forma triângulo')