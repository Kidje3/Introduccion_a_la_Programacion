# ejercicio 5


##  Definir una función llamada sonFactores que tome un entero n y una lista de enteros, y
##  devuelva True si los números de la lista son factores de n (es decir, si n es divisible por todos
##  ellos).




def sonFactores (n, lista):
    for i in range (len(lista)):
        if n % lista[i] != 0:
            return "False"
    return "True"

lista= [4,3,2,8,7]
n= 24

print(sonFactores(n, lista))

