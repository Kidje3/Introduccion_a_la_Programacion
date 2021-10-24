# 2. Hacer un programa que dada una cadena ingresada por el
# usuario indique la cantidad de vocales.

palabra=input(str("ingrese una cadena"))

vocales="aeiou"
cant=0
nueva=""
for char in palabra:
        if char in vocales:
            nueva=nueva+char

print(len(nueva))







