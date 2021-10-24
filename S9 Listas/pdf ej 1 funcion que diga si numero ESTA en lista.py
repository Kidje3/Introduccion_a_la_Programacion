#  Hacer una función que recibe una lista y un entero e
#  indique si el entero está en la lista.





#hay 2 maneras de recorrer la lista para buscar si el entero esta o no
# en el primer caso, recorremos por elemenos, si elemento de la correspondiente iteracion
#es igual al numero buscado, en este caso 9, va a retornar yes. sigue iterando si no lo encuentra,
# sale de la iteracion y return "no"


def numEstaEnLista(lista, entero):
    for elemento in lista:
        if elemento == entero:
            return ("yes")
    return ("no")

lista=[2, 6 , 9 , 34, 87]
entero= 8

# print(numEstaEnLista(lista, entero))



# para este caso, recorremos la lista en un rango, cuyo numero del rango es el len de la lista
# y con un if preguntamos: si lo que va a parenciendo en la ubicacion de la lista, es igual al entero
# return yes , de lo contrario, termina sale del if y del for, y retorna "no"

def numEstaEnLista2 (lista, entero):
    for i in range (len(lista)):
        if lista[i] == entero:
            return "yes"

    return "no"

print(numEstaEnLista2(lista, entero))







