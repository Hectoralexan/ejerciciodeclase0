precio = float(input('coloque el precio del producto: '))
descuento = 0.1
if precio >= 100 :
    print('aplica descuento')

else:
    print('no aplica descuento')
    
    
resultado = precio * descuento
print('descuento de:',resultado)