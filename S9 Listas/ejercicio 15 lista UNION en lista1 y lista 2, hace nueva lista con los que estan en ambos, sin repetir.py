# ejercicio 15

## Definir una función llamada union que tome dos listas sin repetidos y devuelva una nueva lista
## que contenga los elementos de ambas listas. Ojo, la lista de retorno debe no tener repetidos.

def union (lista1,lista2):
    lista3=lista1+lista2
    nueva=[]
    for n in lista3:
        if n not in nueva:
            nueva.append(n)
    print (nueva)



lista1= [4,6,33,21,"zapato",1]
lista2= ["perro", "zapato", 4,7,49,1]


union(lista1,lista2)






