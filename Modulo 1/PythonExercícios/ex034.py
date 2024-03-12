salario_atual = float(input('Informe seu salario: '))
salario_minimo = 1.250
if salario_atual <= salario_minimo:
    aumento = salario_atual * (10 / 100)
    novo_salario = salario_atual + aumento
    print('Se novo salario com aumento de 10% é {}R$'.format(novo_salario))
else:
    aumento = salario_atual * (15 / 100)
    novo_salario = salario_atual + aumento
    print('Seu novo salario com aumento de 15% é {}R$'.format(novo_salario))
