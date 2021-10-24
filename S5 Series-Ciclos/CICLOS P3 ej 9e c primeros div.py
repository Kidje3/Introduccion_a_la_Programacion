# Hacer un programa que permita al usuario elegir dos números positivos c y n y luego
# muestre en pantalla los primeros c divisores de n.




# ej P3-9e)
# PROMEROS C dividores de n

c=int(input("Ingrese la cantidad de divisores que necesita ver"))
n=int(input("Ingrese el numero del cual quiere saber los divisores"))

contadordivisores=0
i=1

while(contadordivisores<c and i<=n):
    if(n%i==0):
        contadordivisores=contadordivisores+1
        print (contadordivisores,"- divisor de ",n,"es ",i)
    i=i+1
if contadordivisores<c:
    print( "no hay mas divisores")