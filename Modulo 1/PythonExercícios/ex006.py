print('===== DOBRO, TRIPLO E RAIZ QUADRADA')
n = int(input('Informe um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}'.format(n, d))
print('O triplo de {} vale {}'.format(n, t))
print('A raiz quadrada de {} é {:.2f}'.format(n, r))


# OUTRA FORMA DE FAZER - Usando menos variaveis

# n = int(input('Digite um numero: ')
# print('O dobro de {} vale {}.'.format(n,(n*2)))
# print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), (n**(1/2))))

