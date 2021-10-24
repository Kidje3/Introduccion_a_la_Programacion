animales=["gato", "perro", "raton"]

i=0

while (i<len(animales)):
    print(animales[i])
    i=i+1



for i in range (len(animales)):
    print (animales[i])


for elementos in animales:
    print(elementos)


# dado un numero construye una lista con sus divisores propios:



# funcion donde damos un numero y nos devuelve los divisores propios.

def divisoresPropios(numero):
    divisorespropios=[]
    for i in range (1,numero):
        if (numero%i==0):
            divisorespropios.append(i)
    return divisorespropios

numero=int (input("ingrese un numero"))
print(divisoresPropios(numero))



