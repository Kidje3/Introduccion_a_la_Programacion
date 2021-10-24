##  5 Hacer una funcion que reciba dos listas, una con notas y otra con los apellidos de los estudiantes
##  que la obtuvieron y devuelva el o la estudiante con la mayor nota
##  (suponer que no hay notas repetidas)


# funcion que retorna el numero maximo de una lista
def maximo (lista):
    elMaximo=lista[0]
    for elem in lista:
        if elem > elMaximo:
            elMaximo= elem

    return elMaximo

# funcion que da la posicion de un elemento en la lista
def damePosiciones(elem,lista):
    nueva=[]
    for i in range (len(lista)):
        if elem == lista[i]:
            nueva.append(i)
    return nueva




apellidos= ["garcia,", "vasquez", "rolon", "fernandez", "casanova"]
notas=     [  8    ,       9     ,   1    ,     9,         5      ]



mayorNota=maximo(notas)  # guardo en variable la mayor nota
listapos= damePosiciones(mayorNota, notas)   # guardo en variable la posicion de mayor notas (lista)
print("la mayor nota es: ", mayorNota )
print("los que la obtuvieron son: ")

for pos in listapos:        # recorro la lista, para buscar segun los indices que me da, imprimir apellidos.
    print(apellidos[pos])