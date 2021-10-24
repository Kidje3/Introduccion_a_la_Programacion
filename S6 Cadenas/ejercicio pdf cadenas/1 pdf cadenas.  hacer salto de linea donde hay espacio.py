# ejercicio 1 cadenas:
# Hacer un programa que reciba una frase y muestre una a una todas las palabras que la componen.
# Ejemplo:
# frase=”Nos los representantes de la Nacion Argentina”
# debe mostrar:
# Nos
# los
# representenates
# de
# la
# Nacion
# Argentina

frase=input("ingrese una frase")

nueva=""
for char in frase:
    if char == " ":
        char= "\n"
    nueva= nueva + char
print(nueva)


