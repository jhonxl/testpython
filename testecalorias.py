print('Possui calorias ou não?')
print('Esse é um medidor básico de calorias, poucos alimentos estão listados.')
comida = input('Escreva o nome de um alimento: ')
if comida == 'Pizza':
	print('Uma pizza possui 266 calorias.')
elif comida == 'Hamburguer':
	print('Um hamburguer possui 295 calorias.')
elif comida == 'Frango':
	print('Um frango possui 239 calorias.')
elif comida == 'Banana':
	print('Uma banana possui 89 calorias.')
elif comida == 'Maçã':
	print('Uma maçã possui 52 calorias.')
elif comida == 'Laranja':
	print('Uma laranja possui 47 calorias.')
elif comida == 'Pêra':
	print('Uma pêra possui 57 calorias.')
else:
	print('Desconheço as calorias!')