#ejercicio 6


## Defnir una funcion que tome una lista y devuelva True si tiene al menos un elemento repetido,
## y False en caso contrario.





# lo que hace esta funcion es recorre una lista, si el elemento no esta en nueva lo agrega
# luego compara la longitud de lista y nueva, si son iguales es que no saco ninguna repeticion

def tieneRepetido(lista):
    nueva=[]
    for i in range(len(lista)):
        if lista[i] not in nueva:
            nueva.append(lista[i])
    if len(lista)== len(nueva):
        return False
    else:
        return True


lista= [1,2,8,7,36,48]


print(tieneRepetido(lista))


