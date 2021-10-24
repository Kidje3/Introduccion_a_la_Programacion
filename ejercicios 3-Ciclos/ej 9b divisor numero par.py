# b)  Hacer un programa que permita al usuario elegir un número positivo n y luego
#      muestre en pantalla todos los divisores pares de n.


numero=int(input("ingrese un numero positivo"))


 #if numero > 0:


b=1

while b<numero:
    for i in range (1, numero+1):
        if numero%i==0:
            print (i, "es divisor par de numero= ", numero)
            b=b+1

