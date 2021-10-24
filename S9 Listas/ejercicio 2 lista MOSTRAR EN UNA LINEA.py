#ejercicio 2

##  Definir una función llamada mostrarEnUnaLinea que tome una lista de enteros y muestre
##  todos sus elementos en una linea separados por espacios


def mostrarEnUnaLinea (lista):
    for  i in range (len(lista)):
        print(lista[i], " " ,  end="")




lista=  ["auto", "casa", "celular", "manzana", 38, "bebe"]

mostrarEnUnaLinea(lista)



