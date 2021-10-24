#  Hacer un programa que reciba un número n (n > 0) y muestre las n primeras
# potencias de 2. Por ejemplo, si el usuario ingresa 6, el programa mostrará: 1 2 4 8
#  16 32.




i=1

potencia=1

cont=0
while cont<3:
    cont=cont+1
    n=int(input("ingrese un numero mayor a 0"))
    if n>0:
        while i<=n:
            print(potencia)
            potencia=2**i
            i=i+1
    else:
        print("tu numero ingresado no es mayor a 0, volve a ingresar un numero")
    if cont==3 and n<0:
        print("Se te acabaron las oportunidades")
    if cont==3 and n>0:
        print("acertaste en la ultima oportunidad")


















