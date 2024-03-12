print('===== REAJUSTE SALARIAL =====')
s = float(input('Informe seu sálario: '))
a = (s * 15) / 100
ns = s + a
print('Seu novo salario com aumento de 15% é {}'.format(ns))


# OUTRA FORMA DE FAZER - Usando menos variaveis

#salario = float(input('Informe seu sálario: R$'))
#novosalario = salario + (salario * 15 / 100)
#print('Um fincionario que ganhava R${}, com aumento de 15% de aumento, passa a receber R${:.2f}'.format(salario, novosalario))
