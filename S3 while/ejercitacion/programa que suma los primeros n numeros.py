# Hacer un programa que sume los primeros n naturales múltiplos de 5 y determine la cantidad mínima de
# términos necesarios para superar un valor tope que se solicita previamente al usuario.



n=int(input("Cuantos numeros naturales multiplo de cinco desea sumar"))
tope=int(input("Determinar un numero tope de sumas"))



contador=1
acum=0
suma=0

bandera=True
while contador<=n and bandera==True:
    acum=acum+1
    if acum%5==0:
        contador=contador+1

        suma=suma+acum

        if suma>tope:
            bandera=False
            print("la cantidad sumada que no supera el tope es ", suma-acum)

# prueba de escritorio con 6 y tope 85 me da el numero 75



















