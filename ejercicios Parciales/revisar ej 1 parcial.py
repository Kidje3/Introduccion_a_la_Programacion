## Ejercicio 1:
## Hacer una función que reciba un entero n e indique cuál es la distancia máxima que separa dos divisores
## primos de n consecutivos.
## Por ejemplo, si n vale 66, sus divisores primos ordenados son 2, 3 y 11. La distancia máxima es 8.

def divisoresnumero (n):
    divisoresnumero=[]
    for i in range (2,n):
        if n%i==0:
            divisoresnumero.append(i)
    return divisoresnumero

def numeroprimo(num):
    numprimo=0
    cant=0
    for i in range (1,num+1):
        if num%i==0:
            cant=cant+1
    if cant==2:
        return True
    else:
        return False

def listaprimos(lista):
    listaprimos=[]
    for element in lista:
        if numeroprimo(element) == True:
            listaprimos.append(element)
    return listaprimos

def distancia(lista):
    distanciamayor=0
    for i in range (len(lista)-1):
        if lista[i] >lista[i+1]:
            a=lista[i]-lista[i+1]
        else:
            a=lista[i+1]-lista[1]

        if a > distanciamayor:
            distanciamayor=a
    return (distanciamayor)

def distanciaMaxima (n):
    lista2=divisoresnumero(n)
    listaprimo=listaprimos(lista2)
    distancia2=distancia(listaprimo)
    return distancia2
n=100
print(distanciaMaxima(n))















