# 3. Hacer un programa que dados un caracter y una cadena indique la cantidad de aparciones
#  de dicho caracter en la cadena.


cadena=input("ingrese una cadena")
caracter=input("ingrese un caracter")


nueva=""
for letra in cadena:
    if letra == caracter:
        nueva=nueva+letra

print(len(nueva))


