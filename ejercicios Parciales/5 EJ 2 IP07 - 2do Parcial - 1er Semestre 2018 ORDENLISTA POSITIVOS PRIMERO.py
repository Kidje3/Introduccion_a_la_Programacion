# ejercicio 2

##  a) Dada una lista de números reales (distintos de 0), escribir una función que devuelva una
##  nueva lista ubicando los números positivos al comienzo.

## Ejemplo: lista_entrada = [3.0, -2.5, -1.8, 25.2, -18.0, 2.53, 4.99]
## Devuelve: lista_salida = [3.0, 25.2, 2.53, 4.99, -2.5, -1.8, -18.0]

## b) Hacer un programa que muestre la lista nueva, utilizando la función creada en (a).

lista= [3.0, -2.5, -1.8, 25.2, -18.0, 2.53, 4.99]


def ordenLista (lista):
    listanueva=[]
    listanueva2=[]
    for num in lista:
        if num>0:
            listanueva.append(num)
        if num<0:
            listanueva2.append(num)
    lista_salida=listanueva+listanueva2

    return lista_salida

print(ordenLista(lista))

