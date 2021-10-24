# ejercicio 28

# Escribir un programa que pida al usuario una cadena y una letra y reemplace las apariciones
# de dicha letra por asteriscos. Por ejemplo, si el usuario ingresa:
# programador tendria que ser p*og*amado*

palabra= input("ingrese una palabra")

letra= input ("ingrese una letra")

nueva=""
for char in palabra:
    if char not in letra:
        nueva=nueva+char
    else:
        if char in letra:
            nueva= nueva + "*"

print (nueva)


