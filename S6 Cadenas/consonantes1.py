#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Luis
#
# Created:     11/09/2018
# Copyright:   (c) Luis 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# cantidad de consonantes (NO VOCALES)
palabra=input ("Ingrese palabra")

n=0
for letra in palabra.lower() :
    if not(letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u"):
        n=n+1


print ("la palabra ",palabra, "tiene ", n, "consonantes")