import random


w=random.randint(1,100)
cont=0
bandera=True
while(cont<3 and bandera):
    m=int(input("Ingrese un entero entre 1-100"))
    if(m==w):
        print("adivino")
        bandera=False
    else:
        print("no adivino, intente de nuevo")
        cont=cont+1
if(bandera):
    print("ya gastastes las 3 opciones, el numero era",w)