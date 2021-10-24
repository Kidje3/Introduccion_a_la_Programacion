# ejercicio 12

##  Escribir una función llamada intercambiar que tome una lista de números s y dos enteros
##  positivos a y b menores que la longitud de la lista y cambie el elemento ubicado en s[a] por el
##  elemento ubicado en s[b]. Ojo, esta función no debe devolver una lista, sino modifcar la que
##  toma como parámetro.

# usar auxiliares en lista
# posicion 2 ---> 31  tiene que ir el 56
# posicion 8----> 56  tiene que ir el 31

def intercambiar (lista,a , b):
    aux=s[a]
    s[a]=s[b]
    s[b]=aux

    return lista

s= [4,6,31,21,84,5,8,77,56,3,24,21]
a=2
b=8

print(s)
print(intercambiar(s,a,b))
print(s)
