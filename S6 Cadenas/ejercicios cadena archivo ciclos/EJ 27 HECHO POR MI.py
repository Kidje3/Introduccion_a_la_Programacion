# 4- Hacer un programa que reciba una palabra e indique si en la misma hay 2 vocales seguidas.
# ejemplo "novia" si tiene 2 vocales seguidas.


palabra= input("ingrese una frase ")

vocales="aeiouAEIOU"

bandera= False

cant=0
for char in palabra:
    if char in vocales:
        cant=cant+1
        if cant==2:
            bandera= True
    else:
        cant=0

if bandera == True:
    print("si hay 2 vocales seguidas")

else:
    print ("no hay 2 vocales seguidas")



