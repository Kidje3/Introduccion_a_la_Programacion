# Ej Palabras.
# Hacer un programa que reciba una frase y muestre la palabra más larga.

frase = "Nos los representantes de la Nacion Argentina"
masLarga=""
posibleLarga=""
for le in frase+" ":                  # recorre la letra en la frase
    if le != " " :                    # si la letra no es un espacio ir formando la "posibleLarga"
        posibleLarga = posibleLarga + le
    else:
        if len(posibleLarga) > len(masLarga) :       # si la "posibleLarga" es mas grande que maslarga,  maslarga pasa a ser "posibleLarga"
            masLarga = posibleLarga
        posibleLarga=""                              # vuelve la palabra a "" cero, para que genere una nueva palabra, y compare  la nueva "posiblelarga" con la ultima "mas larga"
    print(posibleLarga)
print("La palabra mas larga es",masLarga)
