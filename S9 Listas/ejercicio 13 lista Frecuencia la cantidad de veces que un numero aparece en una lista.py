# ejercicio 13

##  Escribir una función llamada frecuencia que tome una lista de enteros s y otro entero n como
##  parametros y devuelva la cantidad de veces que aparece n en s.


def frecuencia (lista, n):
    cont=0
    for elem in lista:
        if elem == n:
            cont=cont+1
    return(cont)


s=[3,21,6,3,4,7,84,3,24,24]
n=24

print(frecuencia(s,n))