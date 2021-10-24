#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      lsv 0
#
# Created:     10/09/2018
# Copyright:   (c) lsv 0 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# PRIMOS

n=int(input("Ingrese numero natural"))

i=1
div=0

while(i<=n):
    if(n%i==0):
        div=div+1
#        print(i)
    i=i+1

if(div==2):
    print(n,"SI es primo")
else:
    print(n,"NO es primo")