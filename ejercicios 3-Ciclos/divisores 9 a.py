# Hacer un programa que permita al usuario elegir un número positivo n y luego
# muestre en pantalla todos los divisores de n

# ej 20 es divisible por 1,2,4,5,10,20

# 20//1,  20//2, 20//3

n= int(input("ingrese un numero positivo"))



b=1
while b<n:


    for i in range (1, n+1):
        if n%i==0:
            print(i,"es divisor de ", n)
        b=b+1





