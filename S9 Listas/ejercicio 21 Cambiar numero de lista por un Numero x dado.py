# ejercicio 21

##  Definir una función que tome una lista de números s y un número decimal x y cambie todos
##  los elementos menores que x por 0.

#  ej:  para [1, 4.1, 6.3, 2, 3.2, 8]

# el la lista debe pasar a ser:

# s = [0, 4.1, 6.3, 0, 3.2, 8]


def cambiarNumX0 (lista, numero):
    for i in range (len(lista)):
        if lista[i]< numero:
            lista[i]= 0
    return lista

s = [1, 4.1, 6.3, 2, 3.2, 8]
x=3.1

print(cambiarNumX0(s,x))

print (s)


