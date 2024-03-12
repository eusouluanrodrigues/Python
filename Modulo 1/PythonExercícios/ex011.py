print('===== PINTANDO PAREDE =====')
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('A parede informada tem dimensão de {} x {} e sua área é de {}m².'.format(alt, larg, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de  {}l de tinta.'.format(tinta))
