#4. Realice un programa que permita calcular el costo anual del consumo de combustible de un vehículo, si el usuario ingresa la distancia recorrida (Km) anual, el consumo de combustible (L / 100Km) anual y el costo promedio anual del combustible por litros recorridos ($ / L) 
dr=float(input("Ingrese la distancia recorrida:" ))
cc=float(input("Ingrese el consumo de combustible: "))
cpc=float(input("Ingrese el costo promedio por litro de combustible: "))
x=(cc/100)*dr*cpc
print("El costo anual de su combistible es de:", x)
#Geraldine  Diaz