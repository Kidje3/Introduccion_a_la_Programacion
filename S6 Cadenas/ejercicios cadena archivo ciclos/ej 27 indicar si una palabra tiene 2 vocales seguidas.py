#  ejercicio 27     Escribir un programa que pida al usuario una cadena e indique si esta posee un diptongo (dos vocales unidas).


# vocales seguidas

palabra=input("Ingrese palabra")
vocales="aeiouAEIOU"
bandera=False
cont=0
for char in palabra.lower():
    if char in vocales:
        cont=cont+1
        if(cont==2):
            bandera=True

    else:
        cont=0  # en este caso, hay que reiniciar el contador a 0, porque si no , va a pasar por alto las consontantes, pero va a seguir contando las vocales.

if bandera == True:
    print("la palabra",palabra,"SI tiene 2 vocales seguidas")
else:
    print("la palabra",palabra,"NO tiene 2 vocales seguidas")
