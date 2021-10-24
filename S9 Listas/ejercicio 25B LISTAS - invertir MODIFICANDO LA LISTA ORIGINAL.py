##  ejercicio 25:
##
##  definir una funcion llamada invertirMod(lista), que reciba y modifique dejando sus elementos
##  en orden inverso
##  ejemplo:
##  frutas= ["banana", "durazno", "manzana", "naranja", "pera", "zapallo"]
##  frutas=["zapallo", "pera", "naranja", "manzana", "durazno", "banana"]



#invertir lista modificando la lista

def intercambiar(lista,a,b):
    aux=lista[a]
    lista[a]=lista[b]
    lista[b]=aux



def invertir(lista):
    for i in range (len(lista)//2):
        intercambiar(lista,i,len(lista)-1-i)






frutas=["banana","durazno","manzana","naranja","pera","zapallo"]

print(frutas)
invertir(frutas)
print(frutas)