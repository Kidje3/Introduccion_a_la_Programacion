#  9  f) Hacer un programa que permita al usuario elegir dos números positivos c y n y luego
#       muestre en pantalla los últimos c divisores de n.

# los ultimos divisores seran 10,5,2,1 = los ultimos 2 son ---10 , 5 ---


n=int(input("ingrese un numero positivo"))
c=int(input("ingrese la cantidad de los ultimos  divisores de n"))


cont=1
h=0

print ("los ultimos ", c, "divisores de ", n, "son: ")

while cont<n:
    for i in range (n,0,-1):
        if n%i==0 and h<c :
            h=h+1
            print(i)

        cont=cont+1


