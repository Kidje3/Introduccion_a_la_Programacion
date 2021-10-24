#  1. Hacer un programa que dada una cadena ingresada por el usauario
#  indique la cantidad de apariciones de la letra "a"
# en este caso lo adapte al ej 26 que pide que el usuario ingrese un caracter.


cadena= input("ingrese una palabra")
caracter=input("ingrese caracter")

cant=0
for char in cadena:
    if char == caracter:
        cant=cant+1

print(cant)






