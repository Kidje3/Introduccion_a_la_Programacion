# Modificar la lista eliminando los elementos cuyo valor es par #



##def sacarParesMAL(lista):
##    for i in range(len(lista)):
##        print(lista,"voy a controlar posición",i,"valor",lista[i])
##        if lista[i]%2==0:
##            lista.pop(i)

def sacarParesBIEN(lista):
    i=0
    while i<len(lista):
        print(lista,"voy a controlar posición",i,"valor",lista[i])
        if lista[i]%2==0:
            lista.pop(i)
        else:
            i=i+1
# Modificar la lista
#eliminando los elementos cuyo valor es par #
lista=[1,2,4,6,8,9,10,4,6,3]
print("ORI",lista)
sacarParesBIEN(lista)
print("FIN",lista)
#resultado lista=[1,9,3]