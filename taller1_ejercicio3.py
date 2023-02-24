#3. Realice un programa donde se solicite al usuario escribir el precio final de un artículo o producto, con el que después calculará e imprimirá en pantalla el valor del IVA y el valor bruto (precio antes de IVA) del artículo o producto.
pf=float(input("Ingrese el precio total de su compra: "))
iva=pf*(0.19)
vb=pf-iva
print("El valor del iva de su compra corresponde a :",iva,"El precio real de su producto es: ",vb)
#Geraldine  Diaz