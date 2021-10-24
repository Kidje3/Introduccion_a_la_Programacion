#  Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
#  potencias de n. Por ejemplo, si el usuario ingresa 4, el programa mostrará: 1 4 27
#  256. Es decir, 1**1  2**2  3**3  4**4


n=int(input("ingrese un numero mayor a 0"))

i=1

potencia=1

if n>0:

    while i<=n:

        potencia=i**i
        print(potencia)
        i=i+1

else:
    print("tu numero no es mayor a 0")



