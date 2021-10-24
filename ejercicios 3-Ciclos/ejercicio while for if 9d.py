#   d)  Hacer un programa que permita al usuario elegir un número positivo n y luego
#       muestre en pantalla la suma de los divisores de n.

#  1 2 5 10 =  18

n=int(input("Ingresar un numero positivo"))

cont=1
sumadivisores=0

while cont<n:
    for i in range (1, n+1):
        if n%i==0:
            sumadivisores=sumadivisores+i
        cont=cont+1

print( sumadivisores )

