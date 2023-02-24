#2. Realice un programa que calcule el índice de masa corporal de una persona, donde le solicite al usuario la estatura en cm y el peso en Kg. Después imprima como resultado el índice de masa corporal mediante un mensaje que diga “Su IMC es valor” redondeado con dos decimales. 
#Fórmula: peso (kg) / [estatura (m)]2
peso=float(input("Ingrese su peso en kg: "))
estatura=float(input("Ingrese su estatura en metros : "))
ims=peso/(estatura**2)
print("Su indice de masa corporal es: ")
print(ims)
#Geraldine  Diaz