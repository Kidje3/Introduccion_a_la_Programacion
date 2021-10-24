# ejercicio 17

##  Definir una función llamada mcd que tome dos enteros positivos y devuelva el máximo común
##  divisor usando funciones de los ejercicios anteriores.
# prueba: 20----> 1 , 2, 4,5,10
#         30----> 1, 2, 3, 5,6,10,15


# busca los divisores de un numero
def divisores(entero):
    divisoresenteros=[]
    for i in range (1,entero):
        if entero % i == 0:
            divisoresenteros.append(i)

    return (divisoresenteros)

#divisores(30)

# busca el elemento mas grande de una lista
def maxElemento (lista):
    maximo=lista[0]
    for i in range (len(lista)):
        if lista[i] > maximo:
            maximo=lista[i]
    return maximo

# en la funcion principal, se fija que divisores hay en comun los mete en nuevalista, y buscar el MAYOR.
###########################################################
#funcion maximo comun divisor

def mcd(a,b):
    listanueva=[]
    a=divisores(a)
    b=divisores(b)
    for i in a:
        if i in b:
            listanueva.append(i)

    return maxElemento(listanueva)


#a=20
#b=30
a=12
b=18


print(mcd(a,b))


####################################################################











