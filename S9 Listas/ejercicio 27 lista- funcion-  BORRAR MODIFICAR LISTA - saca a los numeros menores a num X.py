## Ejercicio 27 Borrar chicos

##   Hacer una función llamada sacarMenorX, que reciba una lista y un valor X, y MODIFIQUE la lista
##   eliminando los valores cuyo valor sea inferior a X.

##    ejemplo:

##    lista = [0.1, 0.2, 0.25, 1.25, 0.78, 0.35, 2.8 ] X=1.0 ==>> debe quedar: lista = [1.25, 2.8 ]



# la funcion busca un numero menor a X, si lo encuentra lo borra, y sigue buscando en la misma posicion 0
# en cambio (else) si el numero es mayor a X, incrementa el i, para que busque en la siguiente posicion

def sacarMenorX(lista, X):
    i=0
    nums=lista
    while i < len(lista):
        if nums[i] < X:
            nums.pop(i)
        else:
            i=i + 1
    return lista

lista = [0.1, 0.2, 0.25, 1.25, 0.78, 0.35, 2.8 ]

X=1.0
print(sacarMenorX(lista, X))

