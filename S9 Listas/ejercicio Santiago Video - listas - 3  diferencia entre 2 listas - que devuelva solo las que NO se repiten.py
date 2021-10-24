##  3  Hacer una funcion que reciba dos listas y devuelva la diferencia entre ellas
##    [5,4,2,8,1,3] [4,8,9,1] debe devolver [5,2,3]

def diferenciaListas (lista1, lista2):
    lista3=[]
    lista4=[]
    for i in lista1:
        if i not in lista2:
            lista3.append(i)
    for i in lista3:
        if i not in lista4:
            lista4.append(i)
    return lista4

a=[5,4,2,8,1,3,2,3,1,1,1]
b=[4,8,9,1,1,1,1]
print(diferenciaListas(a,b))
print(a)
print(b)



