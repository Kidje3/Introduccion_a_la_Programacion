# Ej Palabras.
# Hacer un programa que reciba una frase y muestre la palabra más larga.

frase = "Nos los representantes de la Nacion Argentina"
masLarga=""
pal=""
for le in frase+" ":
    if le != " " :
        pal = pal + le
    else:
        if len(pal) > len(masLarga) :
            masLarga = pal

    print(pal)
print("La palabra mas larga es",masLarga)
