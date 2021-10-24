# ejercicio 4

##  Denifinir una función llamada laMasCorta que tome dos listas y devuelva la que tenga menos
##  elementos. Si tienen igual cantidad, deberá devolver la primera.


def laMasCorta (lista1, lista2):
    if len(lista1) <= len(lista2):
        return lista1
    else:
        return lista2


lista1= [1,2,3,4,5,6,7,8,21,33,45,12,13]


lista2= [1,2,3,4,5,6,7,8,9,10,11,12]


print(laMasCorta(lista1,lista2))





