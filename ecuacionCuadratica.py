import math

def ecuacionCuadratica (a,b,c): 
    x1 = ((b*-1) + (math.sqrt((b**2)+(-4*a* c))))/(2*a)
    x2 = ((b*-1) - (math.sqrt((b**2)+(-4*a* c))))/(2*a)
    print ("x1: ", x1)
    print ("x2: ", x2)


valorA = float(input("Ingrese el valor de A:\n"))
valorB = float(input("Ingrese el valor de B:\n"))
valorC = float(input("Ingrese el valor de C:\n"))

ecuacionCuadratica(valorA,valorB,valorC)

print ("*******************Resultado**********")


