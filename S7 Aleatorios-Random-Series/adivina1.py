import random


w=random.randint(1,100)
print(w)  # - solo para pruba
cont=0

while(cont<3):
    m=int(input("Ingrese un entero entre 1-100"))
    if(m==w):
        print("adivino")
        cont=3
    else:
        cont=cont+1
        print("no adivino, TE QUEDAN", 3-cont, "intentos")
