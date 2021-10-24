# b) Realizar un programa que calcule la cantidad de números ABUNDANTES que existen entre 1 y 100
# (incluídos ambos).


cantabundantes=0
for h in range (1,101):

    cont=1
    sumadivisores=0

    while cont<h:
        cont=1
        sumadivisores=0
        for i in range (1, h):
            if h%i==0:
                sumadivisores=sumadivisores+i
            cont=cont+1



    if sumadivisores > h:
        cantabundantes=cantabundantes + 1
        print("el numero", h, "es abundante")
        print("la cantidad de numeros abundantes son ", cantabundantes)



