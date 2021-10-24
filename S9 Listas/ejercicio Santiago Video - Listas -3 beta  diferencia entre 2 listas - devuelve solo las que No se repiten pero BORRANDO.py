# alternativa de ejercicio donde borro algo de una lista

##  3  Hacer una funcion que reciba dos listas y devuelva la diferencia entre ellas
##    [5,4,2,8,1,3] [4,8,9,1] debe devolver [5,2,3]

# veo si el entero esta en la lista
def esta (entero,lista):
    for elem in lista:
        if elem == entero:
            return True

#pregunt en que posicion se encuentra cierto elemento
def damePosicion(elem, lista):
    for i in range (len(lista)):
        if elem== lista[i]:
            return i

# recorro la lista 2, si esta en la lista 1, la saco- segun la posicion que fui a buscar.
def diferenciaLista(lista1,lista2):
    nueva=lista1
    for elem in lista2:
        if esta (elem,nueva):
            # lo saco
            pos=damePosicion(elem,nueva)
            nueva.pop(pos)
    return nueva



a=[5,4,2,8,1,3]
b=[4,8,9,1]
print(diferenciaLista(a,b))

