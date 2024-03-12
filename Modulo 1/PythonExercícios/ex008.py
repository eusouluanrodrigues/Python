print('===== CONVERSOR DE MEDIDAS =====')
medida = float(input('Informe uma distancia em  metro: '))
cm = medida * 100
mm = medida * 1000
km = medida * 100000
hm = medida / 10000
dam = medida / 10
dm = medida * 10
print("A media de {:.1f}m corresponde a:".format(medida))
print('{:.2f} Centímetro'.format(cm))
print('{:.2f} Milímetro'.format(mm))
print('{:.2f} Quilômetro'.format(km))
print('{:.2f} Hectômetro'.format(hm))
print('{:.2f} Decâmetro'.format(dam))
print('{:.2f} Decímetro'.format(dm))
