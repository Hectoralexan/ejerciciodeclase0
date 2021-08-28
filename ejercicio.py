precio = float(input('coloque el precio del producto: '))
descuento = 0.1
if precio >= 100 :
    print('aplica descuento')
resultado = precio * descuento
else:
    print('no aplica descuento')
    resultado = 0
    

print('descuento de:',resultado)
