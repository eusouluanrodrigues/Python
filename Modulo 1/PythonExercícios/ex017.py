import math
co = float(input('Informe o Cateto Aposto: '))
ca = float(input('Informe o Cateto Adjacente: '))
hip = (co ** 2 + ca ** 2) ** (1/2)
print('O comprimento da hipotenusa é {}'.format(math.sqrt(hip)))


# COM IMPORTAÇÃO
"""
import math
co = float(input('Informe o Cateto Aposto: '))
ca = float(input('Informe o Cateto Adjacente: '))
hi = math.hypot(co, ca)
print('O comprimento da hipotenusa é {}'.format(hip)
"""