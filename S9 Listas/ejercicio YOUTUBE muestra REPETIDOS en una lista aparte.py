#  ejercicio youtube

# encontrar los numeros repetidos de una lista:

numeros= [2,3,4,3,5,9,8,7,2]

repetidos=[]
archivo=[]


def repetidos (lista):
    repetidos=[]
    archivo=[]

    for n in numeros:
        if n not in archivo:
            archivo.append(n)

        else:
            repetidos.append(n)
    print(repetidos)
    print(archivo)

repetidos(numeros)

