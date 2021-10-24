##  4- Hacer una función que reciba una lista y devuelva otra
##  solo con los elementos sin repeticiones

lista= [1,2,2,3,3,5,8,7,9,6,21,26,2,21,100]

def sinRepeticiones (lista):
    nueva=[0]
    for i in range (len(lista)):
        if lista[i] not in nueva:
            nueva.append(lista[i])
    return nueva


# print (sinRepeticiones(lista))


# esta funcion recorre las posiciones de "lista", y pregunta si no esta en nueva, la agrega.
# notese que recorro la posicion, pero toma lo que hay dentro de la posicion. lista[i]



# en cambio en esta otra opcion, recorro solo la lista por elementos, y no por posicion,
# si el elemento no esta en la lista nueva, lo agrego.


def sinRepeticiones2 (lista):
    nueva=[]
    for elemento in lista:
        if elemento not in nueva:
            nueva.append(elemento)
    return nueva

print (sinRepeticiones2(lista))


print(lista)








