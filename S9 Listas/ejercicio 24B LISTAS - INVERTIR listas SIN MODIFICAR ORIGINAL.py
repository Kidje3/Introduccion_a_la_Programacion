##  ejercicio 24
##
##  definir una funcion llamada invertirNueva(lista), que reciba una lista y devuelva una nueva lista
##  con sus elementos en orden inverso

##  ejemplo:    frutas=["banana", "durazno", "manzana", "naranja", "pera", "zapallo"]
##	            nueva=["zapallo", "pera", "naranja", "manzana", "durazno", "banana"]


def invertirNueva(lista):
    nueva=[]
    for pos in range (len(lista)-1,-1,-1):
        nueva.append(lista[pos])
    return nueva

frutas=["banana", "durazno", "manzana", "naranja", "pera", "zapallo"]

nueva=invertirNueva(frutas)

print(nueva)

print (frutas)
