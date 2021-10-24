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

pal=input("Ingrese palabra")
nueva=""
for letra in pal:
    nueva=letra+nueva
print(pal, nueva)
