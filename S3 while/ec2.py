#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lsv0
#
# Created:     31/08/2019
# Copyright:   (c) lsv0 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

print("Este programa calcula ax^2 + bx + c = 0")

a = float(input("Ingrese el valor de a"))
b = float(input("Ingrese el valor de b"))
c = float(input("Ingrese el valor de c"))
print("ingreso a=",a,"b=",b,"c=",c)
if(a != 0):

    discriminante = b*b - 4*a*c

    #precondicion a != 0
    if(discriminante > 0):
        x1 = (-b +(discriminante)**0.5)/(2*a)
        x2 = (-b -(discriminante)**0.5)/(2*a)
        print("Las soluciones son: ", x1, " y ", x2)
    else:
        if(discriminante==0):
            x1 = -b/(2*a)
            print("La solucion es: ", x1)
        #caso discriminante < 0
        else:
            print("La ecuacion no tiene solucion")

else:

    print("tarea para el hogar")





