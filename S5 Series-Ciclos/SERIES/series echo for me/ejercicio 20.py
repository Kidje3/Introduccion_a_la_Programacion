# Hacer un programa que simule el juego de la quiniela. El usuario debe elegir un número del
# 0 al 99 y un monto a apostar, si acierta el número gana 70 veces lo apostado. (El número de la
# suerte debe ser elegido al azar)


import random

azar=random.randint(0,99)
print(azar)

n=int(input("ingrese un numero del 0 al 99"))
dinero=int(input("ingrese cuanto dinero quiere apostar"))



if n== azar:
    dinero=dinero*70
    print("usted adivino el numero ganador", n, "obtiene", dinero, "pesos")

else:
    print("no adivino el numero")









