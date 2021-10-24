#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lsv 0
#
# Created:     23/08/2018
# Copyright:   (c) lsv 0 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Ejercicio 17 Practica 1
# Cajero automatico
# Este cajero entrega billetes de $100 -$200 y $500

monto=int(input("Ingrese el monto a extraer, multiplo de 100"))

if(monto%100!=0 or monto<0):
    print("Ud. ingreso : $",monto,"\n el monto es invalido")

else:

    b500=monto//500
    resto=monto%500
    b200=resto//200
    resto=resto%200
    b100=resto//100

    print("el monto es:", monto)
    print(b500,"billetes de $ 500")
    print(b200,"billetes de $ 200")
    print(b100,"billetes de $ 100")

#fin