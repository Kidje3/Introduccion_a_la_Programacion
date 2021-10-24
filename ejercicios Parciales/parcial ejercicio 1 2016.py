##  ejercicio 1 parcial 1semestre 2016
##
##  hacer una funcion que reciba un entero n e indique cual es la distancia maxima que separa
##  dos divisores primos de n consecutivos.
##  Por ejemplo, si n vale 66, sus divisores primos ordenados son 2,3 y 11. La distancia máxima es 8.




# esta funcion crea una lista con los divisores

def divisores(n):
    primos=[]
    for i in range (1,n+1):
        if n%i==0:
            primos.append(i)
    return (primos)

#print (divisores(66))


# primes=[1, 2, 3, 6, 11, 22, 33, 66]


#esta funcion crea una lista con los divisores primos
def divisoresPrimos(lista):
    divPrimos=[]
    for divisores in lista:
        cont=0
        for i in range (1, divisores + 1) :
            if divisores%i==0:
                cont=cont + 1
        if cont == 2:
            divPrimos.append(i)
    return divPrimos


# esta funcion nos da la distancia maxima de los numeros en una lista
def distanciaMax(lista):
    maxDistancia= 0
    for i in range (len(lista)-1):
        lista[i+1]-lista[i] > maxDistancia
        maxDistancia = lista[i+1]-lista[i]
    return maxDistancia

#print(distanciaMax(distmax))


#esta es la funcion principal, donde utiliza todas las funciones para cumplir con el enunciado.

def distanciaMaxima(n):
    divis=divisores(n)
    divisoresp=divisoresPrimos(divis)
    maxd=distanciaMax(divisoresp)
    return maxd

print(distanciaMaxima(88))










