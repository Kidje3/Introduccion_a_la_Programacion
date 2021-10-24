# ejercicio 7

##  Definir una función llamada dondeAparece que tome una lista de enteros y un entero llamado
##  blanco como parámetros, y devuelva el primer índice donde blanco aparece en el arreglo, si lo
##  hace, y -1 en caso contrario

##def dondeAparece (lista, blanco):
##    for i in range (len(lista)):
##        if blanco in lista:
##            print (lista[i])

def dondeAparece (lista, blanco):
    for i in range (len(lista)):
        if lista[i] == blanco:
            return i

    return -1




lista=[2,3,78,31,22,45,14]
blanco=45

print(dondeAparece(lista,blanco))



