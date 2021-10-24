import random


w=random.randint(1,100)
cont=0
bandera=True
while( bandera):
    m=int(input("Ingrese un entero entre 1-100"))
    cont=cont+1
    if(m==w):
        print("adivino, necesito",cont,"opciones")
        bandera=False
    else:
        if(m>w):
            print("no adivino, el numero es menor")
        else:
            print("no adivino, el numero es mayor")


