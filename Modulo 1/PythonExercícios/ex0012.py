print('===== CALCULANDO DESCONTOS =====')
preço = float(input('Informe o preço do produto: R$'))
novo = (preço * 5) / 100
novopreço = preço - novo
print('Na liquidação esse produto tera 5% de desconto e sai por : R${:.2f} '.format(novopreço))


# OUTRA FORMA DE FAZER - Usando menos variaveis
# preço = float(input('Qual é o prelo do produto? R$'))
# novo = preço - (preço * 5 / 100)
# print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${}'.format(preço, novo))