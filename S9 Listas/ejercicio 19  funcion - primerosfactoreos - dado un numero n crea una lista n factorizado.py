# ejercicio 19

##  Definir una función que tome un entero n y devuelva la lista de los primos que aparecen al
##  factorear n. Ejemplo, para 24, la lista debe ser: [2, 2, 2, 3]

def primosfactoreos (n):
    lista=[]
    for i in range (2,n+1):
        while n%i == 0:
            n=n/i
            lista.append(i)
    return lista

n=24
print(primosfactoreos(n))