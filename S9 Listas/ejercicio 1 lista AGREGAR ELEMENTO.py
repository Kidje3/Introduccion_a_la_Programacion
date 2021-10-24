# ejercicio 1

##  Hacer un programa que guarde la siguiente lista en una variable: ["elefante", "jirafa",
##  "mono"], luego pida el nombre de otro animal, lo agregue a la lista e imprima en pantalla el
##  cuarto animal de la lista.


animales= ["elefante", "jirafa","mono"]


def agregarElemento(lista):
    elemento=input("Agregue un animal")
    lista.append(elemento)
    return lista


print("Original  ", animales)
print("Modificado", agregarElemento(animales))




