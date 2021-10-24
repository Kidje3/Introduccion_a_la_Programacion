#ejercicio 6


## Defnir una funcion que tome una lista y devuelva True si tiene al menos un elemento repetido,
## y False en caso contrario.


# cuenta cuantas veces esta el entero en la lista
def cantdeEntEnLista(lista, entero):
    cont=0
    for elem in lista:
        if elem == entero:
            cont=cont+1
    return(cont)

#print(cantdeEntEnLista(lista,2))


# para este caso la funcion pide una lista, la recorre, y mete el primer elemento en el contador
# para saber si se repite, en ese caso retorna true, para el caso contrario retorna false.

def tieneRepetido(lista):
    for elementos in lista:
        a= cantdeEntEnLista(lista, elementos)
        if a >= 2:
            return True
    return False


lista= [1,2,8,7,36,48,48]
print(tieneRepetido(lista))

