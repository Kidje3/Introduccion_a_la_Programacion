

# invertir lista


def invertirNueva(lista):
    nueva=[]
    for pos in range (len(lista)-1,-1,-1):
        nueva.append(lista[pos])
    return nueva

lista=["banana", "durazno", "manzana", "naranja", "pera", "zapallo" ]

print(invertirNueva(lista))







