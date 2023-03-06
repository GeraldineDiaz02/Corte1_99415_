def algoritmo_1():
    a=int(input("Ingrese un numero: "))
    impares = []
    for i in range (1, a+1):
     if i  % 2 !=0:
        impares.append(i)
    print(",".join(map(str,impares)))
    pass
def algoritmo_2():
    b= int(input("Ingrese un número para calcular su factorial :"))
    fac = 1
    for i in range (1, b+1):
        fac *= i
    print(fac)

def algoritmo_3():
    c=int(input("Ingrese un numero: "))
    primos = []
    for i in range (1, c+1):
        es_primo= True
        for j in range (2, i):
         if i % j==0:
            es_primo =False
            break
        if es_primo:
            primos.append(i)
    if c in primos:
        print(c, "Es primo")
    else:
        print(c,"No es primp")
    print("Estos son los numeros primos hasta", c ," son",  ", ".join(map(str, primos)))
    pass
print("1. Algoritmo que imprime todos los numeros impares hata n numero")
print("2. Algoritmo que imprime el numero factorial de n numero")
print("2. Algoritmo que imprime numeros primos hasta n y diga si es primo")
opcion=int(input("Escoja cual de los anteriores algoritmos quiere probar: "))
if opcion == 1:
    algoritmo_1()
elif opcion == 2:
    algoritmo_2()
elif opcion == 3:
    algoritmo_3()
else: 
    print("El dato ingresado no corresponde con las opciones validas: ")
