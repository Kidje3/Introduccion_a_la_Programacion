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

print("Este programa calcula ax + b  = 0")

a = float(input("Ingrese el valor de a"))
b = float(input("Ingrese el valor de b"))
print ("ingreso a=",a,"b=",b)
if(a!=0):
    print("la solucion es: ",-b/a)
else:
    if(b==0):
        print("infinitas soluciones")
    else:
        print("No tiene solucion")