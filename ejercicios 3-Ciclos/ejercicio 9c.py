#  ejercicio 9c Hacer un programa que permita al usuario elegir un número positivo n y luego
#  muestre en pantalla la cantidad de divisores de n



n= int(input("ingrese un numero positivo"))



cont=1
h=0
while cont<n:
    for i in range (1, n+1):
        if n%i==0:
            h=h+1
        cont=cont+1

print(n, "tiene", h, "divisores")