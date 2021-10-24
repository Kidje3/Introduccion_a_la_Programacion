# ORDENAR UNA LISTA DE MAYOR A MENOR

##### SI QUIERO QUE ORDENE DE MENOR A MAYOR SOLAMENTE CAMBIAR EL SIGNO ######


def ordenarMayaMenor (lista):
    for recorrido in range (1,len(lista)):
        for posicion in range (len(lista) - recorrido):
            if lista[posicion] < lista [posicion +1 ]:
                aux=lista[posicion]
                lista[posicion]=lista[posicion+1]
                lista[posicion + 1 ]= aux
    return lista


lista=[4,21,15,3,15,29]

print(ordenarMayaMenor(lista))




