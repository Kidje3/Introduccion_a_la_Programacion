# ejercicio 8

## Hacer una función que tome una lista de números decimales y devuelva el promedio de los
## elementos.


def promedioNumDecimal (lista):
    promedio=0
    for i in range (len(lista)):
        promedio=promedio + lista[i]
    promedio=promedio/len(lista)


    print(promedio)






lista=[1.3, 2.7 ,7.8 ,9.2]

promedioNumDecimal(lista)

