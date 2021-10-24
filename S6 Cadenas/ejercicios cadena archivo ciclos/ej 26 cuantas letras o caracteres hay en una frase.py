# ejercicio 26

# Hacer un programa que dada una palabra y una letra, imprima la cantidad de apariciones de esa letra

palabra= input ("ingrese una palabra")
caracter= input("ingrese una letra")

nueva=""
for char in palabra:
    if char in caracter:
        nueva= nueva + char

print(len(nueva))

