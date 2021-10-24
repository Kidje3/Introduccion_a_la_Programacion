# a) Realizar un programa que dado un número, indique si este es un número ABUNDANTE.


n=int(input("Ingresar un numero positivo"))

cont=1
sumadivisores=0

while cont<n:
    for i in range (1, n):
        if n%i==0:
            sumadivisores=sumadivisores+i
        cont=cont+1

print( sumadivisores )

if sumadivisores > n:
    print("el numero", n, "es abundante")
else:
    print("el numero", n, "no es abundante")