##  3- Hacer una función que reciba una lista de enteros y
##  devuelva el máximo


lista= [10,2,3,4,8,34,49,2,15,102,4,5,8,7,]

def devuelveMax (lista):
    maximo=lista[0]
    for elem in lista:
        if elem > maximo:
            maximo= elem
    return maximo


print(devuelveMax(lista))

################################################################
####  este tambien retorna el maximo pero lo busca por posicion


lista= [10,2,3,4,8,34,49,2,15,102,4,5,8,7,]

def devuelveMax (lista):
    maximo=lista[0]
    for i in range (len(lista)):
        if lista[i] > maximo:
            maximo= lista[i]
    return maximo

print(devuelveMax(lista))