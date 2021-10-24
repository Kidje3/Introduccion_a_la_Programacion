# ejercicio 16

##  Definir una función llamada diferencia que tome dos listas sin repetidos y devuelva una
##  nueva lista que contenga los elementos de la primera que no estén en la segunda.
# en este ejemplo debe devolver: [6,33,21]

def diferencia(lista1, lista2):
    nueva=[]
    for i in lista1:
        if i not in lista2:
            nueva.append(i)
    return nueva



lista1= [4,6,33,21,"zapato",1]
lista2= ["perro", "zapato", 4,7,49,1]


print(diferencia(lista1,lista2))

