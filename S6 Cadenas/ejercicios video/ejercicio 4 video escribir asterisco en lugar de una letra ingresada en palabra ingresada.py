#  4. Hacer un programa que dados un caracter y una cadena muestre la misma cadena con un
#  * en lugar de dicho caracter.
#  ejemplo: programadar                r
#  p*og*amado*


cadena=input("ingrese una cadena")

letra=input("ingrese una letra")

nueva=""
for char in cadena:

    if char == letra:
        char= "*"
    nueva=nueva + char

print(nueva)






