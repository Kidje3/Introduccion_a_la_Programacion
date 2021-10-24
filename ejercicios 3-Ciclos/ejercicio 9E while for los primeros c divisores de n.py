# 9E  Hacer un programa que permita al usuario elegir dos números positivos c y n y luego
# muestre en pantalla los primeros c divisores de n

# 1 2 5 10 = 10   primeros 3 divisores

n=int(input("ingrese un numero positivo"))
c=int(input("ingrese la cantidad de los primeros divisores de n"))


cont=1
h=0

print ("los primeros ", c, "divisores de ", n, "son: ")

while cont<n:
    for i in range (1, n+1):
        if n%i==0 and h<c :
            h=h+1
            print( cont, end=" ")

        cont=cont+1






