#  ejercicio 3

##  Definir una función llamada divisores que tome un entero y devuelva la lista de divisores de
##  ese entero.


def divisores(entero):
    divisoresentero=[]
    for i in range (1,entero):
        if entero % i == 0:
            divisoresentero.append(i)

    print (divisoresentero)

divisores(30)


