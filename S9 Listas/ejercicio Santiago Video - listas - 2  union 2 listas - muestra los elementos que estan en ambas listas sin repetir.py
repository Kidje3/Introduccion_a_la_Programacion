##  2- Hacer una funcion que reciba dos listas y devuelva la union entre ellas
##  [5,4,2,8,1,3] [4,8,9,1] debe devolver [5,4,2,8,1,3,9]

#es una funcion donde devuelve todos los elementos que estan en lista 1 y 2 sin repetir.

def union (lista1, lista2):
    lista3=lista1 + lista2
    lista4=[]
    for i in lista3:
        if i not in lista4:
            lista4.append(i)
    return lista4




    return lista3


lista1=[5,4,2,8,1,3,3,3]
lista2=[4,8,9,1,3]

print(union(lista1,lista2))



