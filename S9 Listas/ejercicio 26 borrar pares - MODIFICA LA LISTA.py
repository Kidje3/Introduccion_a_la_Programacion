##  Ejercicio 26 Borrar pares
##  Dada una lista de números naturales, modificar la lista sacando los elementos cuyo valor sea PAR (o sea,
##  quedan solo los valores impares).
##  ejemplo:
##  lista = [1, 2, 4, 6, 8, 9, 10, 4, 6, 3 ] ==>> debe quedar: lista = [1, 9, 3 ]





def modificarLista (lista):
    i=0
    while i <len(nums):
        if nums[i] % 2 ==0:
            nums.pop(i)
        else:
            i= i + 1
    return nums

nums= [1,2,4,6,8,9,10,4,6,3]
print(modificarLista(nums))








