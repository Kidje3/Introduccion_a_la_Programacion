# ej 2 pdf
# Hacer una función que dado un entero y una lista de
# enteros indique cuantas veces aparece el entero en la
# lista.



lista=[2, 6 , 9 , 34, 87, 6, 6, 6,34]
entero= 34

def cantdeEntEnLista(lista, entero):
    cont=0
    for elem in lista:
        if elem ==entero:
            cont=cont+1
    return(cont)


print(cantdeEntEnLista(lista, entero))







