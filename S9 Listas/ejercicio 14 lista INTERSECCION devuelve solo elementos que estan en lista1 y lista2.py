# ejecicio 14

## Definir una función llamada interseccion que tome dos listas sin repetidos y devuelva una
## nueva lista que contenga sólamente aquellos elementos que estén en ambas listas


def interseccion(lista1, lista2):
    nueva=[]
    for i in lista1:
        if i in lista2:
            nueva.append(i)
    print (nueva)




lista1= [4,6,33,21,"zapato",1]
lista2= ["perro", "zapato", 4,7,49,1]

print(lista1+lista2)
interseccion(lista1,lista2)


