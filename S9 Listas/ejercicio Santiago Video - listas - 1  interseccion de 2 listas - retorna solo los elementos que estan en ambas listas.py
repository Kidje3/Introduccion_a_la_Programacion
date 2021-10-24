##1-   Hacer una funcion que reciba dos listas y devuelva la interseccion entre ellas
##  [5,4,2,8,1,3] [4,8,9,1] debe devolver [4,8,1]




def interseccion (lista1, lista2):
    lista3=[]
    for i in lista1:
        if i in lista2:
            lista3.append(i)
    return lista3




    return lista3

#lista1=[5,4,2,8,1,3]
#lista2=[4,8,9,1]
listaA=[2,4,6,7,3,1,9]
listaB=[1,2,3,4,5,6,78,8,9,0]


print(interseccion(listaA,listaB))
