# ejercicio 18

##  Defnir una función que tome un entero n y devuelva los primeros n primos.


def numeroprimo(x):
    cont=0
    for i in range (1, x+1):
        if x%i==0:
            cont=cont + 1
    if cont >2:
        return False
    else:
        return True

# print(numeroprimo(18))


#############################################

def primerosNprimos (n):
    cont=0
    i=1
    while n>cont:
        i=i+1
        if numeroprimo(i)== True:
            cont=cont+1
            print(i, end=" ")

n=10

primerosNprimos(n)

##############################################
