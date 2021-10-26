# ejercicio 3

##  Escribir una función que reciba dos números enteros, y devuelva una lista con los divisores
##  primos que tienen en común. Se recomienda fuertemente utilizar funciones auxiliares.

##  Ejemplo: para los números 42 ​y 105​, la función debe retornar la lista [3, 7]​, ya que
##  los divisores primos de 42 son 2, 3 y 7 (también son divisores 6, 14 y 21, pero no primos)
##  los divisores primos de 105 son 3, 5 y 7 (también son divisores 15, 21 y 35, pero no primos)



def divisores(n):
    listDivis=[]
    for i in range (2,n):
        if n%i==0:
            listDivis.append(i)
    return (listDivis)

#print(divisores(42))

def numPrimo(num):
    cont=0
    for i in range(1,num+1):
        if num%i==0:
            cont=cont+1
    if cont==2:
        return True

#a=[2, 3, 6, 7, 14, 21]
#b=[3,5,7,15,21,35]

def sonPrimos(lista):
    nueva=[]
    for num in range (len(lista)):
        if numPrimo(lista[num]):
            nueva.append(lista[num])
    return nueva

#print(sonPrimos(b))

#print(sonPrimos(b))
#lista1=[2,3,7]
#lista2=[3,5,7]

def coindicenNums(lista1,lista2):
    dpc=[]
    for i in lista1:
        if i in lista2:
            dpc.append(i)
    return dpc

#print(coindicenNums(lista1,lista2))

def divPrimComun(a,b):
    lista1=divisores(a)
    lista2=divisores(b)
    prim1=sonPrimos(lista1)
    prim2=sonPrimos(lista2)
    coinciden=coindicenNums(prim1,prim2)
    return coinciden

print(divPrimComun(42,105))










